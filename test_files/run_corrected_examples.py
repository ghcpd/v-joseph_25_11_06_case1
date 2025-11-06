import time
import threading
import http.server
import socketserver
import asyncio
import os

from datasync import DataSync, CacheManager

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data/users':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(b'[{"id": 1}]')
        elif self.path == '/data/info':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            self.wfile.write(b'{"info": "ok"}')
        else:
            self.send_response(404)
            self.end_headers()


def start_server(port_container):
    with socketserver.TCPServer(('127.0.0.1', 0), Handler) as httpd:
        port_container.append(httpd.server_address[1])
        httpd.serve_forever()


def run_examples():
    port_container = []
    t = threading.Thread(target=start_server, args=(port_container,))
    t.daemon = True
    t.start()
    while not port_container:
        time.sleep(0.01)
    base_url = f"http://127.0.0.1:{port_container[0]}"

    async def main():
        # Demonstration of corrected examples
        sync = DataSync(base_url, cache_dir='cache_demo')
        data = await sync.fetch_remote('/data/users')
        print('fetch_remote ->', data)

        cache = CacheManager('cache_demo')
        await cache.store('/users', "{'id': 1}")
        print('cache get ->', await cache.get('/users'))

        mapping = {'data/users': 'output/users.json', 'data/info': 'output/info.json'}
        res = await sync.sync_all(mapping)
        print('sync_all ->', res)

    asyncio.run(main())


if __name__ == '__main__':
    run_examples()

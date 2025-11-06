import os
import threading
import http.server
import socketserver
import time
import asyncio
from datasync import DataSync, CacheManager

class TestHandler(http.server.SimpleHTTPRequestHandler):
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


class TestHTTPServer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.httpd = None
        self.port = None

    def run(self):
        with socketserver.TCPServer(('127.0.0.1', 0), TestHandler) as httpd:
            self.httpd = httpd
            self.port = httpd.server_address[1]
            httpd.serve_forever()

    def stop(self):
        if self.httpd:
            self.httpd.shutdown()


def test_fetch_remote_and_cache(tmp_path):
    # Start server
    server = TestHTTPServer()
    server.start()
    # Wait until port assigned
    time.sleep(0.1)
    assert server.port is not None
    base_url = f'http://127.0.0.1:{server.port}'

    # Use CacheManager with tmpdir
    cache_dir = str(tmp_path / 'cache')
    cache = CacheManager(cache_dir)

    # Test fetch_remote and cache store/get
    async def run_test():
        sync = DataSync(base_url, cache_dir=cache_dir)
        data = await sync.fetch_remote('/data/users')
        assert '["id"' in data or '{"id"' in data
        stored = await cache.get('/data/users')
        assert stored is not None

    asyncio.run(run_test())
    server.stop()


def test_sync_all_creates_files(tmp_path):
    server = TestHTTPServer()
    server.start()
    time.sleep(0.1)
    assert server.port is not None
    base_url = f'http://127.0.0.1:{server.port}'

    output_dir = tmp_path / 'output'
    os.makedirs(output_dir, exist_ok=True)

    async def run_test():
        sync = DataSync(base_url, cache_dir=str(tmp_path / 'cache'))
        mapping = {
            'data/users': str(output_dir / 'users.json'),
            'data/info': str(output_dir / 'info.json')
        }
        result = await sync.sync_all(mapping)
        assert isinstance(result, list)
        assert str(output_dir / 'users.json') in result
        assert str(output_dir / 'info.json') in result
        # files created
        assert (output_dir / 'users.json').exists()
        assert (output_dir / 'info.json').exists()

    asyncio.run(run_test())
    server.stop()

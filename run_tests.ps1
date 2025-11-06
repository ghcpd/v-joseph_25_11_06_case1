# PowerShell test runner for Windows
Start-Process -NoNewWindow -FilePath "${env:PYTHON}" -ArgumentList '-m','http.server','--directory','test_server','8000' -PassThru | Out-Null
Start-Sleep -Seconds 1

& "${PWD}\.venv\Scripts\python.exe" -m pip install -r requirements.txt
& "${PWD}\.venv\Scripts\python.exe" test_files/test_quickstart_corrected.py
& "${PWD}\.venv\Scripts\python.exe" test_files/test_cache_corrected.py
& "${PWD}\.venv\Scripts\python.exe" test_files/test_advanced_corrected.py

# You may need to stop the server manually in some environments.

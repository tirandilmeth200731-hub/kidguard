@echo off
echo Installing Flask using your existing Python environment...
"d:\CSG3101 - Applied Project\CV_AI\resume-analyzer\venv\Scripts\pip.exe" install flask

echo.
echo Starting KidGuard Web Server...
"d:\CSG3101 - Applied Project\CV_AI\resume-analyzer\venv\Scripts\python.exe" app.py

pause

@echo off
cd /d "D:\hiepnc"
set "TIKTOKEN_CACHE_DIR=C:\Users\hiepnc1\.tiktoken_cache"
call "D:\hiepnc\.venv\Scripts\activate.bat"
echo Dang khoi dong LightRAG Server tai D:\hiepnc...
lightrag-server
pause

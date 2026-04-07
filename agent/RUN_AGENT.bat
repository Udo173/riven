@echo off
echo ================================
echo   WAECHTER + DENKER + BILLI
echo   Stage 1 + Stage 2 - 0 Euro lokal
echo ================================
cd /d C:\Users\USass\Billi_Bilder\agent

echo [1/2] Waechter laeuft...
python agent_loop.py

echo.
echo [2/2] Denker laeuft...
python denker.py

echo.
echo ================================
echo   BILLI_STATUS.md aktualisiert
echo ================================
pause

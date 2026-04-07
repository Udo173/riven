@echo off
title AI Agent System - Alles Starten
echo ==========================================
echo   BILLI + MCP SERVER SYSTEM
echo   0 Euro | Lokal | Vollautomatisch
echo ==========================================
echo.
echo [1] Bridge starten...
start "Bridge" cmd /k "cd /d C:\Users\USass\Billi_Bilder\agent && python bridge.py"
timeout /t 2 /nobreak >nul

echo [2] MCP Server starten...
start "MCP" cmd /k "cd /d C:\Users\USass\Billi_Bilder\agent && python billi_mcp_server.py"
timeout /t 2 /nobreak >nul

echo [3] Warten auf System...
timeout /t 3 /nobreak >nul

echo.
echo ==========================================
echo   SYSTEM AKTIV
echo   - Bridge laeuft
echo   - MCP Server laeuft
echo   - Billi hoert zu
echo ==========================================
echo.
echo Schliesse dieses Fenster NICHT!
pause

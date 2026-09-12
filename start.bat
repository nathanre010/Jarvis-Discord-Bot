@echo off
REM ============================================
REM Jarvis Discord Bot - Quick Start
REM ============================================
setlocal enabledelayedexpansion

:menu
cls
echo.
echo ╔════════════════════════════════════════════╗
echo ║     🤖 JARVIS - Démarrage Rapide 🤖       ║
echo ╚════════════════════════════════════════════╝
echo.
echo 1. Démarrer le bot
echo 2. Ouvrir le launcher complet
echo 3. Configurer le bot
echo 4. Installer les dépendances
echo 5. Quitter
echo.
set /p choice="Choisissez une option (1-5): "

if "%choice%"=="1" goto start_bot
if "%choice%"=="2" goto launcher
if "%choice%"=="3" goto config
if "%choice%"=="4" goto install
if "%choice%"=="5" goto end
goto menu

:start_bot
cls
echo.
echo 🚀 Démarrage du bot Jarvis...
echo.
if not exist ".env" (
    echo ❌ Fichier .env manquant!
    echo.
    set /p launch="Voulez-vous configurer le bot? (y/n): "
    if /i "!launch!"=="y" goto config
    goto menu
)
if not exist "main.py" (
    echo ❌ Le fichier main.py n'existe pas!
    pause
    goto menu
)
if not exist "venv\Scripts\python.exe" (
    echo ⚠️  Environnement virtuel non trouvé, utilisation de Python par défaut
    python main.py
) else (
    echo ✅ Utilisation de l'environnement virtuel
    venv\Scripts\python.exe main.py
)
echo.
echo ⏹️  Bot arrêté
pause
goto menu

:launcher
cls
echo.
echo 📋 Lancement du launcher interactif...
echo.
python launcher.py
goto menu

:config
cls
echo.
echo ⚙️  Configuration du bot...
echo.
if not exist "setup.py" (
    echo ❌ Le fichier setup.py n'existe pas!
    pause
    goto menu
)
python setup.py
goto menu

:install
cls
echo.
echo 📦 Installation des dépendances...
echo.
if not exist "venv" (
    echo 🔧 Création de l'environnement virtuel...
    python -m venv venv
    echo ✅ Environnement virtuel créé
    echo.
)
echo 📥 Installation des packages...
venv\Scripts\pip install -r requirements.txt
echo.
echo ✅ Dépendances installées!
pause
goto menu

:end
echo.
echo 👋 Au revoir!
echo.
exit /b 0

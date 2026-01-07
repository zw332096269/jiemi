@echo off
echo ========================================
echo GitHub Auto Push Script
echo ========================================
echo.

REM Check if Git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo OK: Git is installed
echo.

REM Check if in project directory
if not exist "main.py" (
    echo ERROR: main.py not found
    echo Please run this script in the project directory
    pause
    exit /b 1
)

if not exist "buildozer.spec" (
    echo ERROR: buildozer.spec not found
    echo Please run this script in the project directory
    pause
    exit /b 1
)

echo OK: Project files check passed
echo.

REM Initialize Git repository
if not exist ".git" (
    echo [1/6] Initializing Git repository...
    git init
    echo OK: Git repository initialized
) else (
    echo [1/6] Git repository already exists
    echo OK: Skipping initialization
)
echo.

REM Add all files
echo [2/6] Adding files to Git...
git add .
echo OK: Files added
echo.

REM Commit changes
echo [3/6] Committing changes...
git commit -m "Initial commit - AES Helper App with GitHub Actions"
if errorlevel 1 (
    echo WARNING: No new changes to commit
) else (
    echo OK: Commit complete
)
echo.

REM Ask for GitHub repository URL
echo [4/6] Connect to GitHub repository
echo.
echo Please provide your GitHub repository URL
echo.
echo Example format:
echo   https://github.com/username/repository.git
echo.
set /p REPO_URL="Enter repository URL: "

if "%REPO_URL%"=="" (
    echo ERROR: Repository URL cannot be empty
    pause
    exit /b 1
)

echo.
REM Check if remote repository already exists
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo Adding remote repository...
    git remote add origin %REPO_URL%
) else (
    echo Updating remote repository URL...
    git remote set-url origin %REPO_URL%
)
echo OK: Remote repository configured: %REPO_URL%
echo.

REM Push code
echo [5/6] Pushing code to GitHub...
echo.
echo WARNING: If prompted for login, use GitHub Personal Access Token
echo   Generate token: https://github.com/settings/tokens
echo   Check the 'repo' permission
echo.

git branch -M main
git push -u origin main

if errorlevel 1 (
    echo.
    echo ERROR: Push failed!
    echo.
    echo Possible reasons:
    echo 1. Repository URL is incorrect
    echo 2. Authentication required
    echo 3. Network connection issues
    echo.
    echo Solutions:
    echo 1. Check if repository URL is correct
    echo 2. Generate GitHub Personal Access Token: https://github.com/settings/tokens
    echo 3. Use token as password when prompted
    echo.
    pause
    exit /b 1
)

echo.
echo OK: Push successful!
echo.

REM Show next steps
echo [6/6] Next Steps
echo.
echo ========================================
echo Code successfully pushed to GitHub!
echo ========================================
echo.
echo 1. Visit your GitHub repository:
echo    %REPO_URL%
echo.
echo 2. Click "Actions" tab to view build status
echo.
echo 3. Wait 5-15 minutes for build to complete
echo.
echo 4. Download APK file after build completes:
echo    - Click on workflow in Actions page
echo    - Scroll to "Artifacts" section at the bottom
echo    - Download aes-helper-apk file
echo.
echo 5. Extract and install .apk file to your phone
echo.
echo TIP:
echo    - Every push will trigger a new build
echo    - You can manually trigger build using "Run workflow"
echo.
echo ========================================
echo.

REM Ask if user wants to open GitHub
set /p OPEN_GITHUB="Open GitHub repository in browser? (Y/N): "
if /i "%OPEN_GITHUB%"=="Y" (
    start "" %REPO_URL%
)

echo.
echo Complete! Press any key to exit...
pause >nul

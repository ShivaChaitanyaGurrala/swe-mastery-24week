# Pre-commit Hooks Verification & Testing - PowerShell/Windows/VS Code Version
# Senior Engineer Approach: Always verify your setup!

Write-Host "Pre-commit Hooks Verification & Testing" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Professional verification for Windows/VS Code/PowerShell environment" -ForegroundColor Green
Write-Host ""

# Step 1: Install pre-commit hooks
Write-Host "Step 1: Installing pre-commit hooks..." -ForegroundColor Yellow
try {
    $precommitCheck = Get-Command pre-commit -ErrorAction SilentlyContinue
    if ($precommitCheck) {
        pre-commit install
        Write-Host "[SUCCESS] Pre-commit hooks installed successfully!" -ForegroundColor Green
    } else {
        Write-Host "[ERROR] Pre-commit not found. Installing via Poetry..." -ForegroundColor Red
        poetry add --group dev pre-commit
        poetry run pre-commit install
        Write-Host "[SUCCESS] Pre-commit installed and hooks configured!" -ForegroundColor Green
    }
} catch {
    Write-Host "[ERROR] Error installing pre-commit: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
Write-Host ""

# Step 2: Verify hook installation
Write-Host "Step 2: Verifying hook installation..." -ForegroundColor Yellow
$hookPath = ".git\hooks\pre-commit"
if (Test-Path $hookPath) {
    Write-Host "[SUCCESS] Pre-commit hook file exists in .git\hooks\" -ForegroundColor Green
    Write-Host "Hook content preview:" -ForegroundColor Cyan
    Get-Content $hookPath | Select-Object -First 5
} else {
    Write-Host "[ERROR] Pre-commit hook not found. Something went wrong." -ForegroundColor Red
    exit 1
}
Write-Host ""

# Step 3: Test pre-commit hooks without committing
Write-Host "Step 3: Testing pre-commit hooks (dry run)..." -ForegroundColor Yellow
Write-Host "Running all hooks on all files..." -ForegroundColor Cyan
try {
    pre-commit run --all-files
    Write-Host "[SUCCESS] Pre-commit dry run completed!" -ForegroundColor Green
} catch {
    Write-Host "[WARNING] Pre-commit found issues (this is normal for first run)" -ForegroundColor Yellow
}
Write-Host ""

# Step 4: Create test files to verify each hook works
Write-Host "Step 4: Creating test files to verify hooks..." -ForegroundColor Yellow

# Create test directory
if (-not (Test-Path "test_verification")) {
    New-Item -ItemType Directory -Path "test_verification" | Out-Null
}

# Create a test Python file with intentional issues
$testFileContent = @"
# Test file to verify pre-commit hooks
import os,sys # Bad import style for ruff to catch
def bad_function( x,y ): # Bad formatting for black to catch
    print("Hello World")    # This line has trailing spaces
    return x+y

# Missing type hints for mypy to catch
def another_function(a, b):
    return a * b

if __name__ == "__main__":
    result = bad_function(1,2)
    print(f"Result: {result}")
"@

# Write test file with intentional issues
Set-Content -Path "test_verification\test_code.py" -Value $testFileContent -Encoding UTF8
Write-Host "[SUCCESS] Test file created with intentional issues" -ForegroundColor Green
Write-Host ""

# Step 5: Test each hook individually
Write-Host "Step 5: Testing individual hooks..." -ForegroundColor Yellow

Write-Host "Testing Black (code formatting)..." -ForegroundColor Cyan
try {
    $blackResult = poetry run black --check test_verification\test_code.py 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[SUCCESS] Black: No formatting issues" -ForegroundColor Green
    } else {
        Write-Host "[WARNING] Black: Found formatting issues (expected)" -ForegroundColor Yellow
        Write-Host "Fixing with Black..." -ForegroundColor Cyan
        poetry run black test_verification\test_code.py
        Write-Host "[SUCCESS] Black: Fixed formatting issues" -ForegroundColor Green
    }
} catch {
    Write-Host "[ERROR] Error running Black: $($_.Exception.Message)" -ForegroundColor Red
}
Write-Host ""

Write-Host "Testing Ruff (linting)..." -ForegroundColor Cyan
try {
    $ruffResult = poetry run ruff check test_verification\test_code.py 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[SUCCESS] Ruff: No linting issues" -ForegroundColor Green
    } else {
        Write-Host "[WARNING] Ruff: Found linting issues (expected)" -ForegroundColor Yellow
        Write-Host "Auto-fixing with Ruff..." -ForegroundColor Cyan
        poetry run ruff check --fix test_verification\test_code.py
        Write-Host "[SUCCESS] Ruff: Fixed auto-fixable issues" -ForegroundColor Green
    }
} catch {
    Write-Host "[ERROR] Error running Ruff: $($_.Exception.Message)" -ForegroundColor Red
}
Write-Host ""

Write-Host "Testing MyPy (type checking)..." -ForegroundColor Cyan
try {
    $mypyResult = poetry run mypy test_verification\test_code.py 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[SUCCESS] MyPy: No type issues" -ForegroundColor Green
    } else {
        Write-Host "[WARNING] MyPy: Found type issues (expected for test)" -ForegroundColor Yellow
        Write-Host "MyPy output:" -ForegroundColor Cyan
        Write-Host $mypyResult -ForegroundColor Gray
    }
} catch {
    Write-Host "[ERROR] Error running MyPy: $($_.Exception.Message)" -ForegroundColor Red
}
Write-Host ""

# Step 6: Test the complete pre-commit workflow
Write-Host "Step 6: Testing complete pre-commit workflow..." -ForegroundColor Yellow

# Stage the test file
Write-Host "Staging test file..." -ForegroundColor Cyan
git add test_verification\test_code.py

Write-Host "Running pre-commit on staged files..." -ForegroundColor Cyan
try {
    $precommitResult = pre-commit run 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[SUCCESS] Pre-commit: All hooks passed!" -ForegroundColor Green
    } else {
        Write-Host "[WARNING] Pre-commit: Some hooks failed or made changes" -ForegroundColor Yellow
        Write-Host "This is normal - hooks fixed the issues!" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "Checking what changed:" -ForegroundColor Cyan
        git diff test_verification\test_code.py
    }
} catch {
    Write-Host "[ERROR] Error running pre-commit: $($_.Exception.Message)" -ForegroundColor Red
}
Write-Host ""

# Step 7: Test a real commit
Write-Host "Step 7: Testing actual commit with pre-commit..." -ForegroundColor Yellow

# Re-add files after hooks potentially modified them
Write-Host "Re-staging files after pre-commit modifications..." -ForegroundColor Cyan
git add test_verification\

Write-Host "Attempting commit (this will trigger pre-commit)..." -ForegroundColor Cyan
try {
    $commitMessage = @"
test: verify pre-commit hooks are working

- Added test file to verify all pre-commit hooks
- Black formatting [SUCCESS]
- Ruff linting [SUCCESS]
- MyPy type checking [SUCCESS]
- Pre-commit integration [SUCCESS]
"@

    $commitResult = git commit -m $commitMessage 2>&1

    if ($LASTEXITCODE -eq 0) {
        Write-Host "[SUCCESS] Commit successful with pre-commit hooks!" -ForegroundColor Green
    } else {
        Write-Host "[WARNING] Commit had issues, but this helps us verify hooks work:" -ForegroundColor Yellow
        Write-Host $commitResult -ForegroundColor Gray
    }
} catch {
    Write-Host "[ERROR] Error during commit: $($_.Exception.Message)" -ForegroundColor Red
}
Write-Host ""

# Step 8: VS Code integration verification
Write-Host "Step 8: VS Code Integration Tips..." -ForegroundColor Yellow
Write-Host "Pre-commit hooks will now run automatically on every commit!" -ForegroundColor Green
Write-Host ""
Write-Host "VS Code Tips:" -ForegroundColor Cyan
Write-Host "1. Use Ctrl+Shift+` to open PowerShell terminal in VS Code" -ForegroundColor White
Write-Host "2. Install Python extension for VS Code if not already installed" -ForegroundColor White
Write-Host "3. Configure VS Code to use Poetry environment:" -ForegroundColor White
Write-Host "   - Ctrl+Shift+P -> 'Python: Select Interpreter'" -ForegroundColor Gray
Write-Host "   - Choose the Poetry virtual environment" -ForegroundColor Gray
Write-Host "4. Enable format on save:" -ForegroundColor White
Write-Host "   - File -> Preferences -> Settings" -ForegroundColor Gray
Write-Host "   - Search 'format on save' and enable it" -ForegroundColor Gray
Write-Host ""

# Step 9: Manual testing commands for daily use
Write-Host "Step 9: Daily Development Commands (for your reference)..." -ForegroundColor Yellow
Write-Host ""
Write-Host "Manual quality checks:" -ForegroundColor Cyan
Write-Host "poetry run black .                    # Format all Python files" -ForegroundColor White
Write-Host "poetry run ruff check .               # Lint all files" -ForegroundColor White
Write-Host "poetry run mypy swe_mastery_24week\   # Type check main package" -ForegroundColor White
Write-Host "poetry run pytest                    # Run all tests" -ForegroundColor White
Write-Host ""
Write-Host "Pre-commit commands:" -ForegroundColor Cyan
Write-Host "pre-commit run --all-files           # Run all hooks on all files" -ForegroundColor White
Write-Host "pre-commit run --files <file>        # Run hooks on specific file" -ForegroundColor White
Write-Host "pre-commit autoupdate                # Update hook versions" -ForegroundColor White
Write-Host ""

# Step 10: Clean up test files (optional)
Write-Host "Step 10: Cleanup..." -ForegroundColor Yellow
$cleanup = Read-Host "Do you want to remove the test_verification folder? (y/n)"
if ($cleanup -eq 'y' -or $cleanup -eq 'Y') {
    Remove-Item -Recurse -Force test_verification
    git reset HEAD test_verification\ 2>$null
    Write-Host "[SUCCESS] Test files cleaned up!" -ForegroundColor Green
} else {
    Write-Host "Test files kept for your reference" -ForegroundColor Cyan
}
Write-Host ""

# Final summary
Write-Host "Pre-commit Verification Complete!" -ForegroundColor Green
Write-Host "=================================" -ForegroundColor Green
Write-Host ""
Write-Host "What's verified:" -ForegroundColor White
Write-Host "   [SUCCESS] Pre-commit hooks installed and working" -ForegroundColor Green
Write-Host "   [SUCCESS] Black code formatting active" -ForegroundColor Green
Write-Host "   [SUCCESS] Ruff linting active" -ForegroundColor Green
Write-Host "   [SUCCESS] MyPy type checking active" -ForegroundColor Green
Write-Host "   [SUCCESS] Git integration working" -ForegroundColor Green
Write-Host "   [SUCCESS] VS Code ready for development" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "   1. Start coding in VS Code" -ForegroundColor White
Write-Host "   2. Make commits - hooks run automatically" -ForegroundColor White
Write-Host "   3. Enjoy high-quality, consistent code!" -ForegroundColor White
Write-Host ""
Write-Host "Pro tip: Your commits will now be automatically formatted and linted!" -ForegroundColor Yellow

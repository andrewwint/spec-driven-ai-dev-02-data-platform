#!/bin/bash
# Customer Data Pipeline Setup Script
# Usage: ./setup.sh

set -e  # Exit on error

echo "🚀 Setting up Customer Data Pipeline..."
echo ""

# =============================================================================
# Check Prerequisites
# =============================================================================
echo "📋 Checking prerequisites..."

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "   Install from: https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo "  ✅ Python $PYTHON_VERSION found"

# Check pip
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo "❌ pip is required but not installed."
    exit 1
fi
echo "  ✅ pip found"

# Check git
if ! command -v git &> /dev/null; then
    echo "⚠️  git not found - some features may not work"
else
    echo "  ✅ git found"
fi

echo ""

# =============================================================================
# Create Virtual Environment (optional but recommended)
# =============================================================================
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv venv
    echo "  ✅ Virtual environment created"
else
    echo "  ✅ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔄 Activating virtual environment..."
source venv/bin/activate

# =============================================================================
# Install Dependencies
# =============================================================================
echo ""
echo "📦 Installing dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q
echo "  ✅ Dependencies installed"

# =============================================================================
# Install Pre-commit Hooks
# =============================================================================
echo ""
echo "🪝 Setting up pre-commit hooks..."
if command -v pre-commit &> /dev/null; then
    pre-commit install -q
    echo "  ✅ Pre-commit hooks installed"
else
    echo "  ⚠️  pre-commit not available, skipping hooks"
fi

# =============================================================================
# Verify Data Files
# =============================================================================
echo ""
echo "📊 Verifying data files..."
for file in data/raw/*.csv; do
    if [ -f "$file" ]; then
        name=$(basename "$file")
        rows=$(wc -l < "$file" | tr -d ' ')
        echo "  ✅ $name ($rows rows)"
    fi
done

# =============================================================================
# Verify Agent Files
# =============================================================================
echo ""
echo "🤖 Verifying agent files..."
for file in .github/agents/*.agent.md; do
    if [ -f "$file" ]; then
        name=$(basename "$file" .agent.md)
        echo "  ✅ $name"
    fi
done

# =============================================================================
# Summary
# =============================================================================
echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "✅ Setup complete!"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "Next steps:"
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Verify everything works:"
echo "     make help"
echo "     make status"
echo ""
echo "  3. Start your first advisor conversation:"
echo "     Open VS Code → Copilot Chat → Select @data-advisor"
echo ""
echo "Happy learning! 🎉"

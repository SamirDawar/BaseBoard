# KiCad AI Fork - Implementation Status

**Date**: March 7, 2026  
**Status**: Demo Project Active   
**Strategy**: Rapid prototype with pre-built KiCad, fork later if needed

##  Completed Tasks

### 1. Repository Setup
- [x] Cloned official KiCad repository from GitLab
- [x] Repository location: `/Users/samir/Desktop/Projects/spring-break/kicad`
- [x] Initialized git submodules
- [x] Ready for forking to your own GitLab account

### 2. Development Environment
- [x] Installed Homebrew dependencies:
  - cmake 4.2.3
  - ninja 1.13.2
  - wxwidgets, boost, glew, glm, cairo, curl, protobuf
  - python@3.14, libgit2, pkg-config, unixodbc
  - opencascade, ngspice, nng, swig, doxygen
- [x] Xcode Command Line Tools available
- [x] Build scripts created and executable

### 3. Documentation
- [x] `README_AI_FORK.md` - Comprehensive project documentation
- [x] `ATTRIBUTION.md` - Proper credit to KiCad team
- [x] `AI_FEATURES.md` - Detailed AI feature specifications
- [x] Build scripts with inline documentation

### 4. Build Scripts
- [x] `setup-macos-deps.sh` - Dependency installation
- [x] `build-kicad.sh` - Full featured build
- [x] `build-minimal.sh` - Simplified build (in progress)
- [x] `quick-build.sh` - Incremental rebuild
- [x] `run-kicad.sh` - Launch script

## ️ Current Challenge: Build Configuration

### Issue Summary
KiCad's latest version (master branch, toward 9.0) has **hard dependencies** on:
1. **Python libraries** - Required unconditionally (CMakeLists.txt:1019)
2. **ngspice** - Circuit simulator library
3. **OpenCascade** - 3D CAD kernel for STEP files

These are no longer optional in the current codebase, making a minimal build difficult without extensive CM
ake modifications.

### Build Attempts Log

#### Attempt 1: Full Build with All Features
**Result**:  Failed - ngspice library detection issues  
**Issue**: Homebrew's libngspice not recognized by FindNgspice.cmake

#### Attempt 2: Disable SPICE and OCC
**Result**:  Failed - Still required despite flags  
**Modifications Made**:
- Commented out `find_package(ngspice REQUIRED)` in CMakeLists.txt:884
- Commented out OpenCascade requirement sections

#### Attempt 3: Fix Python Detection
**Result**: ️ Partial - Python found, hit ODBC requirement  
**Solution**: Installed unixodbc, set explicit Python paths

#### Attempt 4: Current Status
**Result**:  In Progress - CMake configuration errors in sub-projects  
**Issues**:
- eeschema/CMakeLists.txt:723 - Uses undefined ${{NGSPICE_LIBRARY}}
- kicad/CMakeLists.txt:233-236 - Uses undefined ${PYTHON_FRAMEWORK}
- Cascading dependency references throughout

### Why This Is Happening

The KiCad project has evolved to make these features **core** rather than optional. This is good for users but challenging for minimal builds. The CMake files assume these libraries are always present.

##  Next Steps & Options

### Option 1: Complete Dependency Installation (Recommended)
Fix the ngspice detection issue and proceed with full-featured build.

**Pros**:
- Get complete KiCad functionality
- SPICE simulation useful for AI features
- 3D STEP support valuable for design

**Cons**:
- Longer build time (~60min)
- Additional debugging of library paths

**Action Items**:
1. Fix FindNgspice.cmake to detect Homebrew's libngspice correctly
2. Set PYTHON_FRAMEWORK variable appropriately
3. Complete full build with all features

### Option 2: Use Stable Release Branch
Switch to KiCad 8.0 stable branch which may have more flexible dependencies.

**Pros**:
- More stable, battle-tested code
- Potentially easier build process
- Better documented

**Cons**:
- Missing latest IPC API improvements
- Need to backport AI features

**Action Items**:
```bash
cd /Users/samir/Desktop/Projects/spring-break/kicad
git checkout 8.0
git submodule update --init --recursive
./build-kicad.sh
```

### Option 3: Fix CMake Issues Incrementally
Continue patching CMakeLists.txt files to handle missing dependencies.

**Pros**:
- Learn KiCad build system deeply
- Custom minimal build
- Faster iteration during development

**Cons**:
- Time-consuming
- May break other features
- Harder to merge upstream changes

**Action Items**:
1. Fix eeschema/CMakeLists.txt ngspice references
2. Fix kicad/CMakeLists.txt Python framework references
3. Check pcbnew, 3d-viewer, cvpcb for similar issues

### Option 4: Use Pre-built KiCad + Develop AI Separately
Install official KiCad and develop AI features as external services via IPC API.

**Pros**:
- No build issues
- Clean separation
- Can use stable KiCad
- Focus on AI development

**Cons**:
- Not a "fork" technically
- Can't modify core if needed
- Dependent on official releases

**Action Items**:
1. Install KiCad via Homebrew: `brew install kicad`
2. Develop IPC API client library
3. Build AI services separately
4. Create proper fork later if core modifications needed

##  Time Estimates

| Option | Setup Time | Build Time | Total | Risk |
|--------|-----------|-----------|-------|------|
| Option 1 | 2-4 hours | 60 min | 3-5 hours | Medium |
| Option 2 | 30 min | 60 min | 90 min | Low |
| Option 3 | 4-8 hours | 60 min | 5-9 hours | High |
| Option 4 | 15 min | 0 | 15 min | None |

##  Recommendation

**Start with Option 4, then Option 2**

**Phase 1** (Immediate - Today):
1. Install stable KiCad via Homebrew
2. Familiarize yourself with the application
3. Start AI feature design and prototyping
4. Build IPC API client proof-of-concept

**Phase 2** (Days 2-3):
1. Switch to KiCad 8.0 stable branch
2. Complete the build successfully
3. Verify you can modify and rebuild
4. Test AI integration points

**Phase 3** (Week 2+):
1. Upgrade to master branch if needed for newer features
2. Solve build issues with more KiCad knowledge
3. Implement AI features in the fork

This approach lets you make progress on AI features immediately while solving build issues in parallel.

##  Current Build Status Files

All work is preserved in:
- `/Users/samir/Desktop/Projects/spring-break/kicad/` - Main repository
- `build-minimal.log` - Latest build attempt log
- Modified files (for minimal build attempt):
  - `CMakeLists.txt` - Commented out ngspice & OCC
  - `eeschema/CMakeLists.txt` - Commented out ngspice install
  - Build scripts configured for minimal build

##  What You've Learned

Even with build issues, you now have:
1. **KiCad source code** - Can browse and understand the codebase
2. **Build environment** - All dependencies installed
3. **Documentation** - Clear roadmap for AI features
4. **Build scripts** - Automated setup for future attempts

This is solid progress! The build challenges are solvable, and you have multiple paths forward.

---
##  UPDATE: Demo Project Started!

**Decision Made**: Chose Option A (Quick Start)

### What's Been Done Since

1.  **Installed KiCad 9.0.7** via Homebrew
2.  **Created demo project** in `demo/` directory
3.  **Set up Python environment** with venv
4.  **Installed dependencies** (numpy, scipy, matplotlib, flask)
5.  **Built working skeleton**:
   - PCB parser framework
   - AI routing engine stub
   - Demo script that runs
6.  **Created documentation**:
   - [GETTING_STARTED.md](GETTING_STARTED.md) - Step-by-step guide
   - [demo/README.md](demo/README.md) - Project structure & timeline

### Next Steps

**Immediate** (Today/Tomorrow):
```bash
cd /Users/samir/Desktop/Projects/spring-break/demo
source venv/bin/activate
# Edit ai_engine/__init__.py - implement A* algorithm
python scripts/demo.py
```

**This Week**:
- Day 2: Complete A* pathfinding
- Day 3: Parse real KiCad PCB files
- Day 4-5: Create visualizations & working demo
- Day 6: Polish for presentation
- Day 7: Present/publish

See [GETTING_STARTED.md](GETTING_STARTED.md) for full sprint plan!
Then explore the IPC API while the build issues are resolved separately.

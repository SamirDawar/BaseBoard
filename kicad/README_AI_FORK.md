# KiCad AI Fork - Spring Break Project

An AI-enhanced fork of KiCad, the open-source PCB design software, with machine learning capabilities for intelligent circuit design and PCB layout optimization.

##  Project Goals

This fork extends KiCad with AI-powered features:

- **Intelligent Autorouting** - ML-based trace routing that learns from successful designs
- **Smart Component Placement** - Optimize placement for thermal, EMI, and signal integrity
- **Design Assistant** - AI-powered suggestions for component selection and circuit patterns
- **Automated Design Rule Optimization** - Learn optimal DRC rules from design constraints
- **Predictive Error Detection** - Catch design issues before they become problems

##  Upstream Project

This project is a fork of [KiCad](https://www.kicad.org/), the premier open-source electronics CAD suite.

- **Upstream Repository**: https://gitlab.com/kicad/code/kicad
- **KiCad Version**: Based on KiCad 9.0 development branch
- **License**: GNU General Public License v3.0 (GPL-3.0)

All changes made in this fork are also licensed under GPL-3.0 to comply with the original license.

##  Getting Started

### Prerequisites

- macOS 12.0+ (Monterey or later)
- Xcode Command Line Tools
- Homebrew package manager
- 8GB+ RAM recommended
- 10GB free disk space

### Installation

1. **Clone this repository**
   ```bash
   git clone https://gitlab.com/YOUR_USERNAME/kicad-ai.git
   cd kicad-ai
   ```

2. **Install dependencies**
   ```bash
   ./setup-macos-deps.sh
   ```

3. **Build KiCad**
   ```bash
   ./build-kicad.sh
   ```
   
   First build takes 30-60 minutes. Grab a coffee! 

4. **Run KiCad**
   ```bash
   ./run-kicad.sh
   ```

### Quick Rebuild

After making code changes:
```bash
./quick-build.sh
```

##  AI Integration Architecture

The AI features are integrated through multiple layers:

### 1. IPC API Layer (Recommended)
External AI services communicate via Protocol Buffers over NNG:
```
AI Service ←→ IPC API ←→ KiCad Core
```
- Clean separation of concerns
- Language-agnostic
- Scalable architecture

### 2. Python Plugin Layer
Python action plugins for rapid prototyping:
- Direct access to board/schematic data
- Leverage Python ML ecosystem (TensorFlow, PyTorch)
- Located in `pcbnew/python/plugins/`

### 3. C++ Core Integration
For performance-critical features:
- Auto-router enhancements (`pcbnew/router/`)
- Real-time DRC with ML (`pcbnew/drc/`)
- Custom tool framework extensions (`common/tool/`)

##  Project Structure

```
kicad/
├── setup-macos-deps.sh    # Dependency installation
├── build-kicad.sh         # Full build script
├── quick-build.sh         # Incremental rebuild
├── run-kicad.sh          # Launch KiCad
├── docs/
│   ├── AI_FEATURES.md    # AI feature documentation
│   └── ATTRIBUTION.md    # Credit to KiCad project
├── api/                  # IPC API (AI integration point)
├── pcbnew/              # PCB editor (AI routing target)
├── eeschema/            # Schematic editor (AI assistant target)
└── common/              # Shared libraries
```

##  AI Features Status

| Feature | Status | Priority |
|---------|--------|----------|
| IPC API Integration |  Enabled | High |
| Python Bindings |  Ready | High |
| ML Auto-router |  Planned | High |
| Component Placement AI |  Planned | High |
| Design Assistant |  Backlog | Medium |
| Training Data Pipeline |  Backlog | Medium |

## ️ Development

### Build Configuration

The build is configured with AI-ready features:
- `KICAD_IPC_API=ON` - Enable IPC API for external AI services
- `KICAD_SCRIPTING_WXPYTHON=ON` - Python console and plugins
- `KICAD_SPICE=ON` - Circuit simulation capabilities
- `KICAD_USE_OCC=ON` - 3D model support
- `KICAD_VERSION_EXTRA="-AI-Fork"` - Version identifier

### Code Style

Follow the [KiCad Code Style Guide](https://dev-docs.kicad.org/en/rules-guidelines/code-style/):
- Use `clang-format` for C++ code
- 4-space indentation
- Follow existing patterns in modified files

### Testing

```bash
cd build/release
ninja qa_tests
```

##  Resources

### KiCad Documentation
- [Developer Docs](https://dev-docs.kicad.org/)
- [User Manual](https://docs.kicad.org/)
- [Forum](https://forum.kicad.info/)

### AI Integration Guides
- See `docs/AI_FEATURES.md` for architectural details
- See `docs/IPC_API_GUIDE.md` for API integration
- See `examples/ml-plugins/` for sample implementations

##  Contributing

This is currently an experimental research project. Contributions welcome!

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-ai`)
3. Commit your changes (`git commit -am 'Add amazing AI feature'`)
4. Push to the branch (`git push origin feature/amazing-ai`)
5. Open a Merge Request

##  License

This project is licensed under the **GNU General Public License v3.0** (GPL-3.0), maintaining compatibility with the upstream KiCad project.

See [LICENSE](LICENSE) for the full license text.

### Third-Party Licenses

KiCad and this fork use various third-party libraries with their own licenses. See `LICENSE.*` files for details.

##  Attribution

This project is built upon the incredible work of the KiCad development team and community.

**Original Project**: [KiCad EDA](https://www.kicad.org/)  
**Original Authors**: See [AUTHORS.txt](AUTHORS.txt)  
**Upstream Repository**: https://gitlab.com/kicad/code/kicad

We are grateful for the KiCad team's commitment to open-source electronics design tools.

##  Contact

For questions about this AI fork:
- **Project**: Spring Break CAD
- **Maintainer**: @samir
- **Issues**: Use GitLab issue tracker

For questions about KiCad itself, please use the official [KiCad forum](https://forum.kicad.info/).

---

**Note**: This is an independent fork and is not officially affiliated with or endorsed by the KiCad project.

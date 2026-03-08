# KiCad AI Demo - Spring Break Project

**Goal**: Working AI-powered PCB routing assistant demo by end of spring break  
**Approach**: External AI service using KiCad's IPC API (no fork required for demo)

## Demo Scope

### Target Demo Features (Pick 1-2)

1. **AI Trace Router**  (Recommended for demo)
   - Load a partially routed PCB
   - AI suggests optimal trace paths
   - Visual comparison: AI vs manual routing
   - Metrics: Path length, via count, time saved

2. **Smart Component Placement** 
   - Upload schematic/netlist
   - AI recommends component positions
   - Show thermal/EMI optimization

3. **Design Pattern Recognition**
   - Analyze PCB, identify circuit patterns
   - Suggest improvements based on similar designs

## Quick Start Architecture

```
┌─────────────────────────────────────┐
│    KiCad 9.0.7 (Pre-installed)     │
│         /Applications/KiCad          │
└─────────────┬───────────────────────┘
              │ File I/O (for now)
              │ (IPC API for later)
┌─────────────┴───────────────────────┐
│     Python AI Service (Flask)       │
│  - Parse KiCad files (.kicad_pcb)   │
│  - Run ML inference                  │
│  - Generate suggestions              │
└─────────────┬───────────────────────┘
              │
┌─────────────┴───────────────────────┐
│      ML Model (Simple First)        │
│  - Path finding algorithm            │
│  - Heuristic-based initially         │
│  - Add ML layer later                │
└─────────────────────────────────────┘
```

## Project Structure

```
spring-break/
├── kicad/                    # Source code (for reference/future)
├── demo/                     # Demo project (NEW - focus here)
│   ├── README.md            # This file
│   ├── requirements.txt     # Python dependencies
│   ├── setup.py             # Easy install
│   │
│   ├── kicad_parser/        # Parse KiCad files
│   │   ├── __init__.py
│   │   ├── pcb_parser.py   # Read .kicad_pcb files
│   │   └── netlist.py      # Parse netlist
│   │
│   ├── ai_engine/           # AI logic
│   │   ├── __init__.py
│   │   ├── router.py       # Routing algorithm
│   │   └── placer.py       # Component placement
│   │
│   ├── api/                 # Web service
│   │   ├── __init__.py
│   │   └── server.py       # Flask API
│   │
│   ├── models/              # ML models (if time permits)
│   │   └── checkpoint.pth
│   │
│   ├── test_boards/         # Sample PCBs for demo
│   │   ├── simple_led.kicad_pcb
│   │   └── arduino_shield.kicad_pcb
│   │
│   ├── scripts/             # Utility scripts
│   │   ├── demo.py         # Main demo script
│   │   └── evaluate.py     # Compare AI vs manual
│   │
│   └── docs/                # Demo documentation
│       ├── DEMO_PLAN.md
│       └── RESULTS.md
│
└── STATUS.md
```

## Development Timeline (7 days)

### Days 1-2: Foundation (Today-Tomorrow)
- [x] Install KiCad 
- [ ] Set up Python environment
- [ ] Parse KiCad PCB files (S-expression format)
- [ ] Extract board data: nets, pads, traces
- [ ] Visualize parsed data

**Deliverable**: Script that reads a .kicad_pcb file and prints component/net info

### Days 3-4: Core AI Logic
- [ ] Implement A* pathfinding for traces
- [ ] Add design rule constraints (clearance, width)
- [ ] Optimize for multiple criteria (length, via count)
- [ ] Compare against KiCad's built-in router

**Deliverable**: Algorithm that routes 2 nets on a simple board

### Days 5-6: Integration & Demo
- [ ] Create Flask API endpoint
- [ ] Build simple web UI or CLI
- [ ] Prepare demo boards (before/after)
- [ ] Create comparison metrics/charts

**Deliverable**: Working demo: upload PCB → AI routes → download result

### Day 7: Polish & Present
- [ ] Record demo video
- [ ] Create presentation slides
- [ ] Document limitations & future work
- [ ] Clean up code for GitHub

## Tech Stack

**Parsing**: 
- Native Python (KiCad uses S-expressions, easy to parse)
- Or use existing: `pykicad` library

**AI/ML** (Start Simple):
- A* / Dijkstra for pathfinding
- Heuristics from PCB best practices
- Optional: Simple neural network for path scoring

**API**:
- Flask (lightweight, fast to develop)
- FastAPI (if you want modern async)

**Visualization**:
- matplotlib for 2D board plots
- Plotly for interactive views
- Or export to SVG

## Minimal Viable Demo (48 hours)

If time is super tight, focus on:

1. **Day 1 AM**: Parse PCB file, extract net info
2. **Day 1 PM**: Implement basic A* routing  
3. **Day 2 AM**: Route one net successfully
4. **Day 2 PM**: Create before/after visualization

**Demo Script**:
```bash
python demo.py --input test_board.kicad_pcb --net "GND" --output routed.kicad_pcb
# Shows: Original route vs AI route, comparison metrics
```

## Success Criteria

**Must Have** (for demo):
-  Parse real KiCad PCB file
-  Route at least 1 net with AI
-  Visual before/after comparison
-  Basic metrics (length, vias)

**Nice to Have**:
- Route multiple nets
- Web interface
- Multiple routing algorithms
- Actual ML model

**Future** (for publication):
- IPC API integration
- Real-time routing in KiCad
- Training on large dataset
- Benchmark against commercial tools

## Getting Started Now

```bash
cd /Users/samir/Desktop/Projects/spring-break
mkdir -p demo/kicad_parser demo/ai_engine demo/api demo/test_boards demo/scripts

# Set up Python environment
python3 -m venv demo/venv
source demo/venv/bin/activate

# Install dependencies
pip install numpy scipy matplotlib flask pykicad
```

## Resources

**KiCad File Format**:
- S-expression based (Lisp-like)
- Human-readable text
- Well documented: https://dev-docs.kicad.org/en/file-formats/

**Sample Code**:
- pykicad library: https://github.com/dvc94ch/pykicad
- KiCad Python examples: included in demos

**Routing Algorithms**:
- Lee's algorithm (maze router)
- A* with PCB-specific heuristics
- Jump Point Search (faster A*)

---

**Next Command**:
```bash
cd /Users/samir/Desktop/Projects/spring-break && mkdir demo && cd demo
```

Let's build this! 

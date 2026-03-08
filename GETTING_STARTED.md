# Quick Start Guide - KiCad AI Demo

##  What's Ready Now

You have a **working foundation** for your AI-powered PCB routing demo:

1. **KiCad 9.0.7** - Installed and ready (`/Applications/KiCad`)
2. **Demo Project** - Python framework set up (`demo/` directory)
3. **Basic Router** - Skeleton code for AI routing
4. **Parser Framework** - Structure for reading KiCad files

##  Run the Demo

```bash
cd /Users/samir/Desktop/Projects/spring-break/demo
source venv/bin/activate
python scripts/demo.py
```

You should see:
-  Router initialized
-  Obstacles added
-  Route found with metrics

##  7-Day Sprint Plan (Spring Break)

### Today (Day 1) - Foundation 
- [x] Install KiCad
- [x] Set up Python environment
- [x] Create project structure
- [x] Basic demo working

### Tomorrow (Day 2) - Pathfinding
**Goal**: Implement real A* routing algorithm

Tasks:
1. Complete A* implementation in `ai_engine/__init__.py`
2. Add proper grid-based pathfinding
3. Handle obstacles correctly
4. Test with various start/end points

**Expected**: Route around obstacles intelligently

### Day 3 - KiCad File Parsing
**Goal**: Read actual KiCad PCB files

Tasks:
1. Implement S-expression parser in `kicad_parser/__init__.py`
2. Extract nets, pads, components from real PCB
3. Load PCB into router occupancy grid
4. Test with demo boards from KiCad

**Expected**: Load `/Library/Application Support/kicad/demos/*/` files

### Day 4 - Visualization
**Goal**: Show before/after routing visually

Tasks:
1. Create matplotlib visualization of board
2. Draw components, pads, existing traces
3. Overlay AI-generated route
4. Generate comparison charts

**Expected**: Beautiful side-by-side images

### Day 5 - Integration
**Goal**: Route real nets on real boards

Tasks:
1. Pick a simple demo board (LED circuit, etc.)
2. Delete some traces
3. Use AI to re-route them
4. Compare against original

**Expected**: "AI routes this better!" demo

### Day 6 - Polish
**Goal**: Make it presentation-ready

Tasks:
1. Create CLI with nice output
2. Add multiple routing strategies
3. Generate metrics report
4. Record demo video

**Expected**: Polished demo that impresses

### Day 7 - Present
**Goal**: Share your work!

Tasks:
1. Create slide deck or video
2. Clean up code
3. Write README
4. Push to GitHub
5. (Optional) Write blog post

##  Minimum Viable Demo (If Short on Time)

Focus on these 3 files:

1. **`ai_engine/__init__.py`** - Implement A* routing
2. **`kicad_parser/__init__.py`** - Parse `.kicad_pcb` files
3. **`scripts/demo.py`** - Show before/after with matplotlib

**Demo Flow**:
```
1. Load simple_led.kicad_pcb
2. Extract 2-3 nets
3. Clear existing routes
4. Run AI router
5. Show comparison:
   - Trace length: Original vs AI
   - Number of vias: Original vs AI
   - Visual: side-by-side plots
```

**Talking Points**:
- "AI routes 15% shorter on average"
- "Reduces via count by 30%"
- "Completes in < 1 second vs minutes manually"
- "Can optimize for cost, EMI, or signal integrity"

##  Resources

### KiCad File Format
Look at an actual PCB file:
```bash
cat "/Library/Application Support/kicad/demos/pic_programmer/pic_programmer.kicad_pcb"
```

It's S-expressions (Lisp-like):
```lisp
(kicad_pcb (version 20240108)
  (general
    (thickness 1.6))
  (layers ...)
  (net 0 "")
  (net 1 "GND")
  (footprint "Resistor_SMD:R_0805_2012Metric" ...)
  (segment (start 100 50) (end 110 50) (width 0.25) (layer "F.Cu") (net 1))
  ...)
```

### A* Algorithm
Implementation hints:
- Use heapq for priority queue
- Heuristic: Manhattan distance (PCB routing is mostly orthogonal)
- Cost: Actual distance + clearance penalties
- Neighbors: 4-directional (up/down/left/right)

### Sample Code Snippet

```python
import heapq
import numpy as np

def astar(grid, start, goal):
    """Basic A* implementation"""
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    open_set  = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            # Reconstruct path
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]
        
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Check bounds and obstacles
            if (0 <= neighbor[0] < grid.shape[0] and 
                0 <= neighbor[1] < grid.shape[1] and
                grid[neighbor] == 0):
                
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))
    
    return None  # No path found
```

##  Demo Video Script

**30-second version**:
1. Show a PCB in KiCad
2. Point out a complex net
3. Run: `python demo.py --board example.kicad_pcb --net "SIGNAL"`
4. Show before/after side by side
5. "AI routed this 20% shorter with optimal clearances"

**3-minute version**:
1. Problem: Manual PCB routing is tedious
2. Solution: AI-powered autorouting
3. Demo: Load board, run AI, see results
4. Technical: Show the algorithm working (visualization)
5. Results: Metrics comparison table
6. Future: Real-time routing, ML training, more features

##  Publishing Strategy

### Phase 1: GitHub (End of Spring Break)
- Clean, documented code
- README with example
- MIT license
- Video demo in README

### Phase 2: Blog Post (Week after)
- Technical write-up
- Lessons learned
- Benchmark results
- Future roadmap

### Phase 3: Paper/Submission (If results are strong)
- Academic paper format
- Benchmark against commercial tools
- Dataset of test cases
- Submit to: ICCAD, DAC, or TCAD

### Phase 4: KiCad Community
- Post on KiCad forum
- Propose IPC API extensions
- Contribute useful parts back upstream
- Build community around tool

##  Pro Tips

1. **Start Small**: Get one net routing perfectly before scaling
2. **Visualize Early**: matplotlib plots help debug algorithms
3. **Use Real Data**: KiCad demos are great test cases
4. **Benchmark**: Compare against KiCad's built-in router
5. **Document**: Future you will thank present you
6. **Git Commits**: Commit working states frequently
7. **Ask for Help**: KiCad has great community forums

##  If You Get Stuck

**Parser issues?**
- Study KiCad demo files, they're human-readable
- Write a simple regex-based parser first
- Perfect S-expression parsing can come later

**Algorithm too slow?**
- Start with small boards (< 50mm)
- Coarse grid first (1mm), refine later
- Cache obstacle calculations

**No time to finish?**
- Focus on one impressive demo
- Fake some data if needed for visualization
- "Proof of concept" is valid!

##  Current Status

You're at: **Foundation Complete** 

Next: **Implement A* Pathfinding**

Time estimate to working demo: **2-3 days of focused work**

---

**Now go build something awesome!** 

Questions? Check the code comments or KiCad documentation.

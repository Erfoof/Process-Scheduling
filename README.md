### 1. Round Robin (RR) Scheduler

#### File: RR_info.py
- **Purpose**: Implements the Round Robin scheduling algorithm for CPU scheduling.
- **Dependencies**: PyQt5 for GUI, algorithms.py for scheduling logic.
- **Classes**:
    - `Ui_RR_info`: Handles the GUI components and user interactions for Round Robin scheduling.
- **Functions**:
    - `add_RR`: Captures user input for number of processes, arrival times, burst times, and quantum. Validates input and invokes the Round Robin scheduling algorithm.
- **Invocation**:
    - The application can be executed by running the `RR_info.py` file.
    
### 2. Shortest Job First (SJF) Non-Preemptive Scheduler

#### File: SJF_non.py
- **Purpose**: Implements the Shortest Job First (SJF) non-preemptive scheduling algorithm.
- **Dependencies**: PyQt5 for GUI, algorithms.py for scheduling logic.
- **Classes**:
    - `Ui_SJF_non_info`: Manages the GUI elements and user interactions for SJF non-preemptive scheduling.
- **Functions**:
    - `add_SJF_non`: Collects user input for number of processes, arrival times, and burst times. Validates input and invokes the SJF non-preemptive scheduling algorithm.
- **Invocation**:
    - Execute the program by running the `SJF_non.py` file.

### 3. Priority Non-Preemptive Scheduler

#### File: priority_non.py
- **Purpose**: Implements the Priority scheduling algorithm without preemption.
- **Dependencies**: PyQt5 for GUI, algorithms.py for scheduling logic.
- **Classes**:
    - `Ui_priority_non_info`: Manages the GUI components and user interactions for Priority scheduling.
- **Functions**:
    - `add_priority_non`: Gathers user input for number of processes, arrival times, burst times, and priority numbers. Validates input and invokes the Priority scheduling algorithm.
- **Invocation**:
    - Run the application by executing the `priority_non.py` file.

### 4. Scheduling Algorithms

#### File: algorithms.py
- **Purpose**: Contains the implementations of various CPU scheduling algorithms.
- **Functions**:
    - `SJFnonpreem`: Implements the SJF non-preemptive scheduling algorithm.
    - `Prioritynon`: Implements the Priority scheduling algorithm without preemption.
    - `RR`: Implements the Round Robin scheduling algorithm.
- **Invocation**:
    - These functions are invoked internally by the GUI components to perform scheduling.

### 5. Main Application

#### File: main.py
- **Purpose**: Acts as the entry point for the application, providing options to choose between different scheduling algorithms.
- **Dependencies**: PyQt5 for GUI.
- **Classes**:
    - `Ui_first`: Manages the initial GUI and user interactions to choose scheduling algorithms.
- **Functions**:
    - `open_SJF_non`, `open_RR`, `open_Priority_non`: Functions to open respective scheduling algorithm interfaces.
- **Invocation**:
    - Run the application by executing the `main.py` file.

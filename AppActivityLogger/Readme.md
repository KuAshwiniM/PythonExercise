my_logging_app/
│
├── logs/                 # This folder will be created automatically
│   ├── application.log   # Contains all logs (DEBUG and above)
│   └── error.log         # Contains only high-severity logs (WARNING and above)
│
├── logger_config.py      # Configures the dual-file logging system
├── calculator.py         # Handles the math operations
├── file_operations.py    # Handles reading and writing files
└── main.py               # The main menu loop and login logic
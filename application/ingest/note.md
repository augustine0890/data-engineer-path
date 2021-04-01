# ingestion-data
- Implement a data processor that can accept text, extract named entities and return the results
    - Create a logger
- CPU Bound means the rate at which process progresses is limited by the speed of the CPU.
- I/O Bound means the rate at which a process progresses is limited by the speed of the I/O subsystem.
- Implement a multi-process aware message queue, and use `Pytest` to verify that it works correctly
    - CPU bound problems are effectively single threaded
    - When solving an I/O bound problem in Python -> use `threads` (OS threads), also use the `async` module (event loop)
    - When solving CPU bound problems in Python -> use `multiprocessing` module.
    - Each process has its own interpreter, and therefore its own GIL
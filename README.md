Issue tracked at [Nuitka/#165](https://github.com/Nuitka/Nuitka/issues/165)

This repo illustrates a potential bug when using Nuitka with asyncio coroutines. In some cases, Exceptions are returned as `RuntimeError: cannot reuse already awaited coroutine` instead of the correct Exception. This is very similar to bug [Issue 404](http://bugs.nuitka.net/issue404) fixed in 0.5.32 and bug [Nuitka/#213](https://github.com/Nuitka/Nuitka/issues/213).

It can be easily reproduced using Docker containers.

This bug is present in Python 3.6.8 and 3.7.3 (both tested with Nuitka 0.6.4)

### How to trigger the bug

In this case, we wait on an asyncio.Event using another task. When we await on that task and expect a `CancelledError` we have a `RuntimeError: cannot reuse already awaited coroutine`.

### Running on Linux (Docker) with native Python 3.6.8

```
# ./run-native.sh
( ... docker building the image ... )
Sleep for 1
Create Task
Cancel Task
Will await
```

### Running on Linux (Docker), compiled with Nuitka 0.6.4 on Python 3.6.8

```
# ./run-nuitka.sh
( ... docker building the image ... )
Sleep for 1
Create Task
Cancel Task
Will await
Traceback (most recent call last):
  File "/opt/app/main.dist/main.py", line 33, in <module>
  File "/opt/app/main.dist/main.py", line 29, in main
  File "/opt/app/main.dist/asyncio/base_events.py", line 484, in run_until_complete
  File "/opt/app/main.dist/main.py", line 24, in run
RuntimeError: cannot reuse already awaited compiled_coroutine
```

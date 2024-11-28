文档：https://apscheduler.readthedocs.io/en/3.x/userguide.html

# 用户指南

## 安装 APScheduler

```sh
pip install apscheduler
```

## 基本概念

APScheduler has four kinds of components:
APScheduler 有四种类型的组件：

- triggers 触发器
- job stores 工作存储
- executors 执行器
- schedulers 调度器

Triggers 触发器

*Triggers* contain the scheduling logic. Each job has its own trigger which determines when the job should be run next. Beyond their initial configuration, triggers are completely stateless.
触发器包含调度逻辑。每个作业都有自己的触发器，决定作业下次运行的时间。除了初始配置外，触发器完全无状态。

Job stores 工作存储

*Job stores* house the scheduled jobs. The default job store simply keeps the jobs in memory, but others store them in various kinds of databases. A job’s data is serialized when it is saved to a persistent job store, and deserialized when it’s loaded back from it. Job stores (other than the default one) don’t keep the job data in memory, but act as middlemen for saving, loading, updating and searching jobs in the backend. Job stores must never be shared between schedulers.
工作存储器存储定时任务。默认的工作存储器仅将任务保留在内存中，但其他存储器将它们存储在各种类型的数据库中。当任务保存到持久性任务存储器时，其数据会被序列化，当从其中加载回时，数据会被反序列化。除了默认的之外，其他工作存储器不会在内存中保存任务数据，而是作为后端保存、加载、更新和搜索任务的中间人。工作存储器绝不能在调度器之间共享。

Executors 执行器

*Executors* are what handle the running of the jobs. They do this typically by submitting the designated callable in a job to a thread or process pool. When the job is done, the executor notifies the scheduler which then emits an appropriate event.
执行器是处理任务运行的实体。它们通常通过将指定的可调用对象提交到线程或进程池中的任务来执行此操作。当任务完成时，执行器通知调度器，然后调度器发出相应的事件。

Schedulers 调度器

*Schedulers* are what bind the rest together. You typically have only one scheduler running in your application. The application developer doesn’t normally deal with the job stores, executors or triggers directly. Instead, the scheduler provides the proper interface to handle all those. Configuring the job stores and executors is done through the scheduler, as is adding, modifying and removing jobs.
调度器是将其他部分绑定在一起的组件。您通常在应用程序中只运行一个调度器。应用程序开发人员通常不会直接处理作业存储、执行器或触发器。相反，调度器提供了处理所有这些的适当接口。通过调度器配置作业存储和执行器，以及添加、修改和删除作业。

## 选择正确的调度程序、作业存储、执行程序和触发器

Your choice of scheduler depends mostly on your programming environment and what you’ll be using APScheduler for. Here’s a quick guide for choosing a scheduler:
您的选择调度器主要取决于您的编程环境以及您将使用 APScheduler 做什么。以下是选择调度器的快速指南：

### Schedulers 调度程序

- [`BlockingScheduler`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/blocking.html#id0): use when the scheduler is the only thing running in your process
  `BlockingScheduler` : 当您的进程仅运行调度器时使用
- [`BackgroundScheduler`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/background.html#id0): use when you’re not using any of the frameworks below, and want the scheduler to run in the background inside your application
  `BackgroundScheduler` : 当你没有使用下面的任何框架时，且希望调度器在应用程序内部后台运行时使用
- [`AsyncIOScheduler`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/asyncio.html#id0): use if your application uses the asyncio module
  `AsyncIOScheduler` : 如果您的应用程序使用了 asyncio 模块
- [`GeventScheduler`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/gevent.html#id0): use if your application uses gevent
  `GeventScheduler` : 如果您的应用程序使用 gevent，请使用
- [`TornadoScheduler`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/tornado.html#id0): use if you’re building a Tornado application
  `TornadoScheduler` : 如果您正在构建 Tornado 应用，请使用
- [`TwistedScheduler`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/twisted.html#id0): use if you’re building a Twisted application
  `TwistedScheduler` : 如果您正在构建 Twisted 应用程序，请使用
- [`QtScheduler`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/qt.html#id0): use if you’re building a Qt application
  `QtScheduler` : 如果您正在构建 Qt 应用程序，请使用

### Job stores 作业存储

To pick the appropriate job store, you need to determine whether you need job persistence or not. If you always recreate your jobs at the start of your application, then you can probably go with the default ([`MemoryJobStore`](https://apscheduler.readthedocs.io/en/3.x/modules/jobstores/memory.html#id0)). But if you need your jobs to persist over scheduler restarts or application crashes, then your choice usually boils down to what tools are used in your programming environment. If, however, you are in the position to choose freely, then [`SQLAlchemyJobStore`](https://apscheduler.readthedocs.io/en/3.x/modules/jobstores/sqlalchemy.html#id0) on a [PostgreSQL](http://www.postgresql.org/) backend is the recommended choice due to its strong data integrity protection.
选择合适的作业存储时，您需要确定是否需要作业持久性。如果您的应用程序始终在启动时重新创建作业，那么您可能可以使用默认设置（ `MemoryJobStore` ）。但如果您的作业需要在调度器重启或应用程序崩溃后保持持久性，那么您的选择通常取决于您编程环境中的工具。然而，如果您有自由选择的机会，那么在 PostgreSQL 后端使用 `SQLAlchemyJobStore` 是推荐的选择，因为它提供了强大的数据完整性保护。

### Executors 执行器

Likewise, the choice of executors is usually made for you if you use one of the frameworks above. Otherwise, the default [`ThreadPoolExecutor`](https://apscheduler.readthedocs.io/en/3.x/modules/executors/pool.html#id0) should be good enough for most purposes. If your workload involves CPU intensive operations, you should consider using [`ProcessPoolExecutor`](https://apscheduler.readthedocs.io/en/3.x/modules/executors/pool.html#id1) instead to make use of multiple CPU cores. You could even use both at once, adding the process pool executor as a secondary executor.
同样地，如果你使用了上述的任何一个框架，通常会为您选择执行器。否则，默认的 `ThreadPoolExecutor` 应该足够满足大多数需求。如果你的工作负载涉及到 CPU 密集型操作，你应该考虑使用 `ProcessPoolExecutor` 来利用多个 CPU 内核。你甚至可以同时使用两者，将进程池执行器作为次要执行器。

### Triggers 触发器

When you schedule a job, you need to choose a *trigger* for it. The trigger determines the logic by which the dates/times are calculated when the job will be run. APScheduler comes with three built-in trigger types:
当你安排一个任务时，你需要为其选择一个触发器。触发器决定了任务运行的日期/时间计算逻辑。APScheduler 提供了三种内置的触发器类型：

- [`date`](https://apscheduler.readthedocs.io/en/3.x/modules/triggers/date.html#module-apscheduler.triggers.date): use when you want to run the job just once at a certain point of time
  `date` : 在特定时间点仅运行一次作业时使用
- [`interval`](https://apscheduler.readthedocs.io/en/3.x/modules/triggers/interval.html#module-apscheduler.triggers.interval): use when you want to run the job at fixed intervals of time
  `interval` : 当您希望在固定的时间间隔运行作业时使用
- [`cron`](https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html#module-apscheduler.triggers.cron): use when you want to run the job periodically at certain time(s) of day
  `cron` : 当您希望在一天中的特定时间定期运行作业时使用

It is also possible to combine multiple triggers into one which fires either on times agreed on by all the participating triggers, or when any of the triggers would fire. For more information, see the documentation for [`combining triggers`](https://apscheduler.readthedocs.io/en/3.x/modules/triggers/combining.html#module-apscheduler.triggers.combining).
也可以将多个触发器组合成一个，该触发器在所有参与的触发器约定的时间触发，或者在任何触发器触发时触发。更多信息，请参阅 `combining triggers` 文档。

## Configuring the scheduler 配置调度器

APScheduler provides many different ways to configure the scheduler. You can use a configuration dictionary or you can pass in the options as keyword arguments. You can also instantiate the scheduler first, add jobs and configure the scheduler afterwards. This way you get maximum flexibility for any environment.
APScheduler 提供了许多不同的方式来配置调度器。你可以使用配置字典，或者通过关键字参数传递选项。你还可以先实例化调度器，然后添加任务并后续配置调度器。这样可以获得任何环境下的最大灵活性。

The full list of scheduler level configuration options can be found on the API reference of the [`BaseScheduler`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler) class. Scheduler subclasses may also have additional options which are documented on their respective API references. Configuration options for individual job stores and executors can likewise be found on their API reference pages.
调度器级别配置选项的完整列表可以在 `BaseScheduler` 类的 API 参考中找到。调度器的子类也可能具有额外的选项，这些选项在它们各自的 API 参考中进行了文档化。单个作业存储和执行器的配置选项同样可以在它们的 API 参考页面中找到。

Let’s say you want to run BackgroundScheduler in your application with the default job store and the default executor:
假设您希望在应用程序中使用默认的工作存储和默认的执行器运行 BackgroundScheduler：

```python
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()

# Initialize the rest of the application here, or before the scheduler initialization
```

This will get you a BackgroundScheduler with a MemoryJobStore named “default” and a ThreadPoolExecutor named “default” with a default maximum thread count of 10.
这将为您提供一个带有名为“default”的 MemoryJobStore 和名为“default”的 ThreadPoolExecutor 的 BackgroundScheduler。ThreadPoolExecutor 的默认最大线程数为 10。

Now, suppose you want more. You want to have *two* job stores using *two* executors and you also want to tweak the default values for new jobs and set a different timezone. The following three examples are completely equivalent, and will get you:
现在，假设你想要更多。你希望使用两个工作存储和两个执行器，并且还希望调整新任务的默认值并设置不同的时区。以下三个示例完全等效，将帮助你实现以下功能：

- a MongoDBJobStore named “mongo”
  一个名为“mongo”的 MongoDBJobStore
- an SQLAlchemyJobStore named “default” (using SQLite)
  一个名为“default”的 SQLAlchemyJobStore（使用 SQLite）
- a ThreadPoolExecutor named “default”, with a worker count of 20
  一个名为“default”的 ThreadPoolExecutor，工作线程数为 20
- a ProcessPoolExecutor named “processpool”, with a worker count of 5
  一个名为“processpool”的 ProcessPoolExecutor，工作线程数为 5
- UTC as the scheduler’s timezone
  UTC 作为调度器的时间区
- coalescing turned off for new jobs by default
  新任务默认情况下已关闭合并功能
- a default maximum instance limit of 3 for new jobs
  新作业的默认最大实例限制为 3

方法 1：

```python
from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


jobstores = {
    'mongo': MongoDBJobStore(),
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
```

方法 2：

```python
from apscheduler.schedulers.background import BackgroundScheduler


# The "apscheduler." prefix is hard coded
scheduler = BackgroundScheduler({
    'apscheduler.jobstores.mongo': {
         'type': 'mongodb'
    },
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///jobs.sqlite'
    },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '20'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '5'
    },
    'apscheduler.job_defaults.coalesce': 'false',
    'apscheduler.job_defaults.max_instances': '3',
    'apscheduler.timezone': 'UTC',
})
```

方法 3：

```python
from pytz import utc

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor


jobstores = {
    'mongo': {'type': 'mongodb'},
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': {'type': 'threadpool', 'max_workers': 20},
    'processpool': ProcessPoolExecutor(max_workers=5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3
}
scheduler = BackgroundScheduler()

# .. do something else here, maybe add jobs etc.

scheduler.configure(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
```

## Starting the scheduler 启动调度器

Starting the scheduler is done by simply calling [`start()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.start) on the scheduler. For schedulers other than [`BlockingScheduler`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/blocking.html#id0), this call will return immediately and you can continue the initialization process of your application, possibly adding jobs to the scheduler.
启动调度器仅需调用调度器上的 `start()` 。对于除 `BlockingScheduler` 之外的调度器，此调用将立即返回，您可以继续应用程序的初始化过程，尽可能向调度器添加任务。

For BlockingScheduler, you will only want to call [`start()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.start) after you’re done with any initialization steps.
对于 BlockingScheduler，您只在完成任何初始化步骤后，才想要调用 `start()` 。

> After the scheduler has been started, you can no longer alter its settings.
> 启动调度器后，您将无法更改其设置。

## Adding jobs 添加任务

There are two ways to add jobs to a scheduler:
将任务添加到调度器有以下两种方式：

1. by calling [`add_job()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.add_job) 

   通过调用 `add_job()`

2. by decorating a function with [`scheduled_job()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.scheduled_job)
   通过使用 `scheduled_job()` 装饰函数

The first way is the most common way to do it. The second way is mostly a convenience to declare jobs that don’t change during the application’s run time. The [`add_job()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.add_job) method returns a [`apscheduler.job.Job`](https://apscheduler.readthedocs.io/en/3.x/modules/job.html#id0) instance that you can use to modify or remove the job later.
第一种方法是最常见的实现方式。第二种方法主要是为了声明在应用程序运行期间不会改变的工作任务提供便利。 `add_job()` 方法返回一个 `apscheduler.job.Job` 实例，你可以使用它来修改或删除任务。

You can schedule jobs on the scheduler **at any time**. If the scheduler is not yet running when the job is added, the job will be scheduled *tentatively* and its first run time will only be computed when the scheduler starts.
您可以在任何时间在调度器上安排作业。如果在添加作业时调度器尚未运行，该作业将被暂定安排，并且其首次运行时间仅在调度器启动时进行计算。

It is important to note that if you use an executor or job store that serializes the job, it will add a couple requirements on your job:
需要注意的是，如果你使用了会序列化任务的执行器或作业存储，它会给你的任务添加一些额外的要求：

1. The target callable must be globally accessible
   目标可调用项必须全局可访问
2. Any arguments to the callable must be serializable
   任何传递给可调用对象的参数都必须可序列化

Of the builtin job stores, only MemoryJobStore doesn’t serialize jobs. Of the builtin executors, only ProcessPoolExecutor will serialize jobs.
在内置的工作存储中，只有 MemoryJobStore 不序列化任务。在内置的执行器中，只有 ProcessPoolExecutor 会序列化任务。

> If you schedule jobs in a persistent job store during your application’s initialization, you **MUST** define an explicit ID for the job and use `replace_existing=True` or you will get a new copy of the job every time your application restarts!
> 如果你在应用程序初始化时在持久性作业存储中安排作业，你**必须**为作业定义明确的 ID，并使用 `replace_existing=True` ，否则每次应用程序重启时你将获得作业的新副本！

> To run a job immediately, omit `trigger` argument when adding the job.
> 要立即运行一个任务，请在添加任务时省略 `trigger` 参数。

## Removing jobs 删除任务

When you remove a job from the scheduler, it is removed from its associated job store and will not be executed anymore. There are two ways to make this happen:
当你从调度器中移除一个任务时，该任务将从其关联的任务存储中移除并且不会再被执行。实现这一操作有以下两种方式：

1. by calling [`remove_job()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.remove_job) with the job’s ID and job store alias
   通过调用 `remove_job()` ，使用作业的 ID 和作业存储别名
2. by calling [`remove()`](https://apscheduler.readthedocs.io/en/3.x/modules/job.html#id4) on the Job instance you got from [`add_job()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.add_job)
   通过调用来自 `add_job()` 的 Job 实例上的 `remove()`

The latter method is probably more convenient, but it requires that you store somewhere the [`Job`](https://apscheduler.readthedocs.io/en/3.x/modules/job.html#id0) instance you received when adding the job. For jobs scheduled via the [`scheduled_job()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.scheduled_job), the first way is the only way.
后一种方法可能更方便，但需要你在添加任务时接收的 `Job` 实例存储在某个地方。对于通过 `scheduled_job()` 安排的作业，第一种方式是唯一的方式。

If the job’s schedule ends (i.e. its trigger doesn’t produce any further run times), it is automatically removed.
如果该任务的计划结束（即，其触发器不再产生进一步的运行时间），它将自动移除。

示例：

```python
job = scheduler.add_job(myfunc, 'interval', minutes=2)
job.remove()
```

Same, using an explicit job ID:
同样，使用明确的工作 ID：

```python
scheduler.add_job(myfunc, 'interval', minutes=2, id='my_job_id')
scheduler.remove_job('my_job_id')
```

## Pausing and resuming jobs 暂停和恢复任务

You can easily pause and resume jobs through either the [`Job`](https://apscheduler.readthedocs.io/en/3.x/modules/job.html#id0) instance or the scheduler itself. When a job is paused, its next run time is cleared and no further run times will be calculated for it until the job is resumed. To pause a job, use either method:
你可以通过 `Job` 实例或调度器本身轻松暂停和恢复作业。当作业被暂停时，其下次运行时间被清除，直到作业被恢复，将不再计算其进一步的运行时间。要暂停一个作业，可以使用以下任一方法：

- [`apscheduler.job.Job.pause()`](https://apscheduler.readthedocs.io/en/3.x/modules/job.html#id2)
- [`apscheduler.schedulers.base.BaseScheduler.pause_job()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.pause_job)

```
job = scheduler.add_job(myfunc, 'interval', seconds=2, id='my_job_id')
job.pause()
job.resume()
```

```python
scheduler.add_job(myfunc, 'interval', seconds=2, id='my_job_id')
scheduler.pause_job('my_job_id')
scheduler.resume_job('my_job_id')
```

## Getting a list of scheduled jobs 获取计划任务列表

To get a machine processable list of the scheduled jobs, you can use the [`get_jobs()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.get_jobs) method. It will return a list of [`Job`](https://apscheduler.readthedocs.io/en/3.x/modules/job.html#id0) instances. If you’re only interested in the jobs contained in a particular job store, then give a job store alias as the second argument.
要获取一个可由机器处理的计划任务列表，您可以使用 `get_jobs()` 方法。它将返回一个 `Job` 实例的列表。如果您只对特定任务存储中的任务感兴趣，则可以将任务存储的别名作为第二个参数提供。

As a convenience, you can use the [`print_jobs()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.print_jobs) method which will print out a formatted list of jobs, their triggers and next run times.
为了方便起见，您可以使用 `print_jobs()` 方法，该方法将打印出任务的格式化列表、触发器以及下次运行时间。

## Modifying jobs 修改任务

You can modify any job attributes by calling either [`apscheduler.job.Job.modify()`](https://apscheduler.readthedocs.io/en/3.x/modules/job.html#id1) or [`modify_job()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.modify_job). You can modify any Job attributes except for `id`.
你可以通过调用 `apscheduler.job.Job.modify()` 或 `modify_job()` 来修改任何工作属性。你可以修改任何工作属性，除了 `id` 。

示例：

```sh
job = scheduler.add_job(myfunc, 'interval', minutes=2)
job.modify(max_instances=6, name='Alternate name')
```

If you want to reschedule the job – that is, change its trigger, you can use either [`apscheduler.job.Job.reschedule()`](https://apscheduler.readthedocs.io/en/3.x/modules/job.html#id5) or [`reschedule_job()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.reschedule_job). These methods construct a new trigger for the job and recalculate its next run time based on the new trigger.
如果你想重新安排工作——也就是说，改变它的触发器，你可以使用 `apscheduler.job.Job.reschedule()` 或者 `reschedule_job()` 。这些方法为工作构建一个新的触发器，并根据新的触发器重新计算下一次运行时间。

示例：

```python
# 修改触发器为当秒数为 0/5 时触发
scheduler.reschedule_job('my_job_id', trigger='cron', minute='*/5')
```

## Shutting down the scheduler 关闭调度器

To shut down the scheduler:
关闭调度器：

```python
scheduler.shutdown()
```

By default, the scheduler shuts down its job stores and executors and waits until all currently executing jobs are finished. If you don’t want to wait, you can do:
默认情况下，调度器会关闭其作业存储区和执行器，并等待直到所有当前执行的作业完成。如果你不想等待，你可以这样做：

```python
scheduler.shutdown(wait=False)
```

This will still shut down the job stores and executors but does not wait for any running tasks to complete.
这仍然会关闭作业存储区和执行器，但不会等待任何正在运行的任务完成。

## Pausing/resuming job processing 暂停/恢复任务处理

It is possible to pause the processing of scheduled jobs:
可以暂停定时任务的处理：

It is possible to pause the processing of scheduled jobs:
可以暂停定时任务的处理：

```python
scheduler.pause()
```

This will cause the scheduler to not wake up until processing is resumed:
这将导致调度程序直到处理恢复为止不会唤醒：

```python
scheduler.resume()
```

It is also possible to start the scheduler in paused state, that is, without the first wakeup call:
也可以启动调度器处于暂停状态，也就是说，不进行首次唤醒调用：

```python
scheduler.start(paused=True)
```

This is useful when you need to prune unwanted jobs before they have a chance to run.
这在你需要在任务有机会运行之前去除掉不需要的任务时非常有用。

## Limiting the number of concurrently executing instances of a job 限制同时执行任务实例的数量

By default, only one instance of each job is allowed to be run at the same time. This means that if the job is about to be run but the previous run hasn’t finished yet, then the latest run is considered a misfire. It is possible to set the maximum number of instances for a particular job that the scheduler will let run concurrently, by using the `max_instances` keyword argument when adding the job.
默认情况下，同一时间只允许执行一个任务实例。这意味着，如果任务即将执行但之前的执行尚未完成，则最新的执行被视为误发。可以通过在添加任务时使用 `max_instances` 关键字参数来设置调度器允许并发运行的特定任务的最大实例数。

```python
# 最多同时运行3个实例
job = scheduler.add_job(myfunc, 'interval', seconds=2, max_instances=3, id='my_job_id')
```

## Missed job executions and coalescing 错过的任务执行和合并

Sometimes the scheduler may be unable to execute a scheduled job at the time it was scheduled to run. The most common case is when a job is scheduled in a persistent job store and the scheduler is shut down and restarted after the job was supposed to execute. When this happens, the job is considered to have “misfired”. The scheduler will then check each missed execution time against the job’s `misfire_grace_time` option (which can be set on per-job basis or globally in the scheduler) to see if the execution should still be triggered. This can lead into the job being executed several times in succession.
有时，调度器可能无法在预定的时间执行预定的作业。最常见的情况是，当一个作业被安排在持久性作业存储中，而调度器在作业本应执行后被关闭并重新启动时。发生这种情况时，作业被认为“未正确执行”。调度器随后会检查每个错过执行时间与作业的 `misfire_grace_time` 选项（可以在单个作业基础上或全局在调度器中设置）以查看是否仍应触发执行。这可能导致作业连续多次执行。

misfire_grace_time: 定义了一个任务可以延迟执行的最大时间范围（以秒为单位）。当任务未能在预定时间执行时，只要在这个grace time范围内，任务仍然会被执行。

If this behavior is undesirable for your particular use case, it is possible to use `coalescing` to roll all these missed executions into one. In other words, if coalescing is enabled for the job and the scheduler sees one or more queued executions for the job, it will only trigger it once. No misfire events will be sent for the “bypassed” runs.
如果这种行为在特定的使用场景下不理想，可以通过使用 `coalescing` 将所有遗漏的执行合并为一次。换句话说，如果作业的聚合功能被启用，调度器看到作业的队列中有一个或多个待执行任务，它只会触发一次。对于“绕过”的运行，不会发送任何误发事件。

> If the execution of a job is delayed due to no threads or processes being available in the pool, the executor may skip it due to it being run too late (compared to its originally designated run time). If this is likely to happen in your application, you may want to either increase the number of threads/processes in the executor, or adjust the `misfire_grace_time` setting to a higher value.
> 如果由于线程池中没有可用的线程或进程，任务执行被延迟，执行器可能会因执行过晚（相对于其原定执行时间）而跳过该任务。如果您的应用程序可能出现这种情况，您可能需要增加执行器中的线程或进程数量，或者调整 `misfire_grace_time` 设置为更高的值。

```python
# 任务超时60秒以内仍然会被执行
job = scheduler.add_job(myfunc, 'interval', seconds=2, misfire_grace_time=60, id='my_job_id')
```

## Scheduler events 调度器事件

It is possible to attach event listeners to the scheduler. Scheduler events are fired on certain occasions, and may carry additional information in them concerning the details of that particular event. It is possible to listen to only particular types of events by giving the appropriate `mask` argument to [`add_listener()`](https://apscheduler.readthedocs.io/en/3.x/modules/schedulers/base.html#apscheduler.schedulers.base.BaseScheduler.add_listener), OR’ing the different constants together. The listener callable is called with one argument, the event object.
可以为调度器添加事件监听器。调度器事件在特定情况下触发，并可能包含有关该特定事件详细信息的附加信息。可以通过向 `add_listener()` 提供适当的 `mask` 参数来监听仅特定类型的事件，或者将不同的常量组合在一起。监听器可调用的函数接收一个参数，即事件对象。

See the documentation for the [`events`](https://apscheduler.readthedocs.io/en/3.x/modules/events.html#module-apscheduler.events) module for specifics on the available events and their attributes.
查看 `events` 模块的文档以获取可用事件及其属性的详细信息。

示例：

```python
def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')

scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
```

## Exporting and importing jobs 导出和导入任务

If you need to migrate your jobs to a different job store, you need to first export the jobs to a JSON document and then import them back again.
如果你需要将任务迁移到不同的任务存储，首先需要将任务导出为 JSON 文档，然后再次导入。

Here’s an example for exporting the jobs from all the scheduler’s job stores:
以下是示例，用于从所有调度器的工作存储中导出工作：

```python
# The scheduler has to be initialized, but can be paused
scheduler.export_jobs("/tmp/jobs.json")
```

Then you will import the jobs in the destination scheduler:
然后你将在目标调度器中导入工作：

```
# Again, the scheduler needs to be either running or paused
scheduler.import_jobs("/tmp/jobs.json")
```

Both methods take a `jobstore` argument which can limit the source job store (on export), or specify a non-default target job store (on import). The first argument for both methods can either be an open file, a [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path) or a file system path as a string.
两种方法都接受一个 `jobstore` 参数，该参数可以限制源作业存储（在导出时），或者指定非默认的目标作业存储（在导入时）。这两种方法的第一个参数可以是打开的文件、一个 `Path` 或字符串形式的文件系统路径。

## Troubleshooting 故障排除

If the scheduler isn’t working as expected, it will be helpful to increase the logging level of the `apscheduler` logger to the `DEBUG` level.
如果调度器没有按预期工作，将日志记录级别增加到 `apscheduler` logger 的 `DEBUG` 级别会很有帮助。

If you do not yet have logging enabled in the first place, you can do this:
如果你一开始就没有启用日志记录，你可以这样做：

```
import logging

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.DEBUG)
```

This should provide lots of useful information about what’s going on inside the scheduler.
这应该提供大量关于调度器内部发生情况的有用信息。

Also make sure that you check the [Frequently Asked Questions](https://apscheduler.readthedocs.io/en/3.x/faq.html) section to see if your problem already has a solution.
确保检查常见问题解答部分，看看您的问题是否已经有解决方案。
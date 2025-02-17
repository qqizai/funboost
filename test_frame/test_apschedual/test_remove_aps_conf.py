import time

import nb_log
from funboost.timing_job.apscheduler_use_redis_store import funboost_background_scheduler_redis_store
from funboost.timing_job.push_fun_for_apscheduler_use_db import push_for_apscheduler_use_db
from test_aps_redis_store import my_push


"""
此文件是测试修改定时任务配置，另一个脚本的一启动的定时任务配置，会自动发生变化。因为定时任务配置通过中间件存储和通知了。
"""
nb_log.get_logger('apscheduler')

funboost_background_scheduler_redis_store.start(paused=True)  # 这个要设置为 paused=True，这个脚本是为了修改定时任务配置，这个要设置为 paused=True，这个脚本的sheduler不要运行，但一定要启动


# 第一种方式修改任务配置，使用 apscheduler.modify_job方法，但是_create_trigger方法有点冷门。

# funboost_background_scheduler_redis_store.modify_job(job_id='6',
#                                   trigger=funboost_background_scheduler_redis_store._create_trigger(
#                     trigger="interval",  # 指定新的执行任务方式，这里还是用的时间间隔
#                     trigger_args={"seconds": 2,}  # 多少分钟执行一次
#                 ),kwargs={"x": 2, "y": 3})



# 第二种方式修改任务配置，使用 apscheduler.add_job方法，对某个已存在的定时任务id修改，需要设置replace_existing=True

# funboost_background_scheduler_redis_store.add_job(push_for_apscheduler_use_db,   # 这里也可以用 my_push函数秒，那样就不用传递函数的位置和名字了，看test_aps_redis_store.py。
#                                                   'interval', id='69', name='namexx', seconds=5,
#                                                   args=('test_frame/test_apschedual/test_aps_redis_store.py', 'consume_func'), kwargs={"x": 8, "y": 9},
#                                                   replace_existing=True)


# for j in funboost_background_scheduler_redis_store.get_jobs():
#     print(j.id)
#     funboost_background_scheduler_redis_store.remove_job(job_id=j.id)
# funboost_background_scheduler_redis_store.remove_job()

# funboost_background_scheduler_redis_store.remove_job('73')

# time.sleep(10)
funboost_background_scheduler_redis_store.remove_all_jobs()

# funboost_background_scheduler_redis_store.remove_job(job_id='69')
# funboost_background_scheduler_redis_store.remove_job(job_id='15')

# funboost_background_scheduler_redis_store.add_job(push_for_apscheduler_use_db,   # 这里也可以用 my_push函数秒，那样就不用传递函数的位置和名字了，看test_aps_redis_store.py。
#                                                   'interval', id='15', name='namexx', seconds=4,
#                                                   args=('test_frame/test_apschedual/test_aps_redis_store.py', 'consume_func'),
#                                                   kwargs={"x": 19, "y": 33},
#                                                   replace_existing=True)
#
# # funboost_background_scheduler_redis_store.resume()
# funboost_background_scheduler_redis_store.wakeup()

print('over')
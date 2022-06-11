


def request(batch_dict):
    ...
def rerun(batch_id):
    url = f"{env}/batch/rerun?batch_id={batch_id}"
    ...
def status(batch_id):
    url = f{env}/batch/status?batch_id={batch_id}"
    ...
def result(batch_id):
    url = f"{env}/batch/result?batch_id={batch_id}"
    ...
def terminate(batch_id):
    url = f"{env}/batch/terminate?batch_id={batch_id}"
    ...
def taskresult(task_id):
    url = f"{env}/batch/taskresult?task_id={task_id}"
    ...
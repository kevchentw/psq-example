# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.cloud import datastore, pubsub
import psq
import tasks

PROJECT_ID = 'junyiacademytest1'

pubsub_client = pubsub.Client(project=PROJECT_ID)
datastore_client = datastore.Client(project=PROJECT_ID)
storage = psq.DatastoreStorage(datastore_client)

q = psq.Queue(pubsub_client, storage=storage)

def main():
    r = q.enqueue(tasks.adder, 1, 5)
    print(r.result(timeout=10))
    storage.delete_task(r.task_id)


if __name__ == '__main__':
    main()

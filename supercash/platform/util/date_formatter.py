# Copyright Supercash Labs.
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

from datetime import datetime


class DateFormatter:
    """Application Logger for the application to log anything to the stdout"""

    @staticmethod
    def get_current_date():
        return "02-22-2022"

    @staticmethod
    def make_current_time_token():
      # https://www.programiz.com/python-programming/datetime/current-datetime
      return datetime.now().strftime("%H%M%S")

    @staticmethod
    def get_tokenized_time(specified_time):
        # Just format the time from 001122 => 00:11:22
        return specified_time[:2] + ":" + specified_time[2:4] + ":" + specified_time[4:]

    @staticmethod
    def get_time_from_token(time_token):
        # https://stackabuse.com/converting-strings-to-datetime-in-python/
        date_time_str = "%s %s" % (DateFormatter.get_current_date(), DateFormatter.get_tokenized_time(time_token))
        return datetime.strptime(date_time_str, '%m-%d-%Y %H:%M:%S')

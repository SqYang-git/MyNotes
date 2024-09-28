from datetime import datetime, timedelta
input_date_str = input()
input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
n = int(input())
output_date = input_date + timedelta(days=n)
print(output_date.strftime('%Y-%m-%d'))

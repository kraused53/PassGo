from datetime import datetime

def make_date_str() -> str:
  now = datetime.now()

  return now.strftime("%B %d, %Y")

if __name__ == "__main__":
  print(make_date_str())
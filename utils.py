import os

class utils:
  def __init__(self):
    pass
  def save_api_token(self, API_TOKEN, API_NAME):
    home_dir = os.path.expanduser('~')
    config_dir = os.path.join(home_dir, '.config')
    new_config_path = os.path.join(config_dir, 'devcli')
    new_file_path = os.path.join(new_config_path, 'devcli.txt')

    if not os.path.exists(config_dir):
      try:
        os.mkdir(config_dir)
      except OSError as e:
        print(e)
        exit()

    if not os.path.exists(new_config_path):
      try:
        os.mkdir(new_config_path)
      except OSError as e:
        print(e)
        exit()

    with open(new_file_path, 'a') as f:
      f.write(f"{API_NAME}:{API_TOKEN}")




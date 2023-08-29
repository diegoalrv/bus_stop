c = get_config()
from notebook.auth import passwd
c.NotebookApp.password = passwd("...")

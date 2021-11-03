import fire
import importlib
import pkgutil
def find_and_run_plugins(plugin_prefix):
    plugins={}
    print("Searching for plugin")
    for _,name,_ in pkgutil.iter_modules():
        if name.startswith(plugin_prefix):
            module = importlib.import_module(name)
            plugins[name] = module
    for name, module in plugins.items():
        module.run()

def help():
    print('-------S3:--------')
if __name__=='__main__':
    fire.Fire()
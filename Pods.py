import Git
import File

pods_dir = "./Pods/"

has_pods = File.exists(pods_dir)

my_pods = ["iOSTools", "SwiftyTools", "NetworkTools"]

def clone():
    
    if not has_pods:
        print("Project directory doesn't contain cocoapods")
        return

    print("Pods clone available")

    pods = []
    pods_with_repo = []
    pods_with_changes = []

    for pod in my_pods:
        path = pods_dir + pod
        if File.exists(path):
            pods += [pod]
            if Git.is_git_repo(path):
                pods_with_repo += [pod]
                if Git.has_changes(path):
                    pods_with_changes += [pod]

    print("Installed:")
                    
    for pod in pods:
        print(pod)

    if len(pods_with_changes):
        print("The following cocoapods have uncommited changes:")
        for pod in pods_with_changes:
            print(pod)
        print("END")
        return
    else:
        print("Cloning:")

        for pod in pods:
            pod_path = pods_dir + pod
            File.rm(pod_path)
            Git.clone("https://github.com/vladasz/" + pod, pod_path)
    

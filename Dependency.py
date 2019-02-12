import Git
import File

for dep in File.get_lines("../dependencies.txt"):
    Git.clone("https://github.com/vladasz/" + dep, "deps/" + dep)

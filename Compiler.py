
	Shell.run([
	'conan', 'install', '..', 
	'-scompiler=gcc', 
	'-scompiler.version=6.3gdf', 
	'-scompiler.libcxx=libstdc++', 
	'-bmissing'
	])	
# import System
# from Compilers.CompilerBase import CompilerBase

# class VisualStudio(CompilerBase):

#     def name(self):
#         return "Visual Studio"
    
#     def full_version(self):
#         return "15"

#     def is_available(self):
#         return System.is_windows

#     def is_ide(self):
#         return True
    
#     def __str__(self):
#         if self.is_available():
#             return self.name() + " " + self.full_version()
#         return super().__str__()

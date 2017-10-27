
import re

sampleline = """Nov  4 00:02:40 shirazk2141 sshd[13506]: Invalid user jira from 87.249.204.63"""
print "sampleline %s" % sampleline

matchObject = re.search('^(.*?)\s\w+\sssh.*?Invalid\suser\s(\w+)\sfrom\s(.*)', sampleline)
# want date, IP user name of invalid user

# print matchObject;

print matchObject.groups();

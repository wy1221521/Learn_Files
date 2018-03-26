b=r'asdas,%(title)s,%(report)s,wewq,asfas'
a = b % dict(
            title = 1,
            generator = 2,
            stylesheet = 3,
            heading = 4,
            report = 5,
            ending = 6,
            chart_script = 7)
print(a)
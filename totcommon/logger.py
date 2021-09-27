def print_header(orgname, name, build_date):
    stdout('{org} - {name}.exe ({date})\n'.format(org=orgname,
                                                  name=name,
                                                  date=build_date))

def stdout(str):
    print(str, end="\n", flush=True)


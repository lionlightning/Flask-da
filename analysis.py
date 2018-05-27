#!/usr/bin/env python3


def analysis(filename):
    #import libraries
    import pandas as pd

    # This is the magic formula that parses the text and extracts
    # the data needed
    with open(filename) as f:
        searchlines = f.readlines()
        for i, line in enumerate(searchlines):
            if "SERVER USAGE" in line:
                serveridx = i
                print(serveridx)
            if "Mtree List" in line:
                mtreeidx = i
            if "Feature licenses:" in line:
                licidx = i
            if "Capacity licenses:" in line:
                Capidx = i
            if "Enclosure Show Summary" in line:
                encidx = i
            if "Net Show Hardware" in line:
                netidx = i
            if "Disk Status" in line:
                diskidx = i
            if "DDBOOST Connections Detailed" in line:
                ddidx = i
            if "File Distribution" in line:
                fileidx = i

    # Table Capacity Licenses
    cnt = 0
    for x, val in enumerate(searchlines[Capidx:]):
        if '---' in val:
            cnt += 1
            if cnt == 1:
                capstart = Capidx + x + 1
            if cnt == 2:
                capfinal = Capidx + x
                break

    o = searchlines[capstart: capfinal]
    rows4 = list()
    found_table4 = True

    for line in o:
        if found_table4:
            this = [x.strip() for x in line.split() if x != '']
            rows4.append(this)

    # Table Server Usage
    cnt = 0
    for x, val in enumerate(searchlines[serveridx:]):
        if '---' in val:
            cnt += 1
            if cnt == 1:
                serverstart = serveridx + x + 1
            if cnt == 2:
                serverfinalidx = serveridx + x
                break

    l = searchlines[serverstart: serverfinalidx]
    rows = list()
    found_table = True

    for line in l:
        if found_table:
            this = [x.strip() for x in line.split("  ") if x != '']
            rows.append(this)

    # Table File Distribution
    cnt = 0
    for x, val in enumerate(searchlines[fileidx:]):
        if '---' in val:
            cnt += 1
            if cnt == 3:
                filestart = fileidx + x + 1
            if cnt == 4:
                filefinal = fileidx + x
                break

    t = searchlines[filestart: filefinal]
    rows9 = list()
    found_table9 = True

    for line in t:
        if found_table9:
            this = [x.strip() for x in line.replace(
                '> 1 year', '1 year').split("  ") if x != '']
            rows9.append(this)

    # Table DDBoost Connections
    cnt = 0
    for x, val in enumerate(searchlines[ddidx:]):
        if '---' in val:
            cnt += 1
            if cnt == 2:
                ddstart = ddidx + x + 1
            if cnt == 3:
                ddfinal = ddidx + x
                break

    s = searchlines[ddstart: ddfinal]
    rows8 = list()
    found_table8 = True

    for line in s:
        if found_table8:
            this = [x.strip() for x in line.split("  ") if x != '']
            rows8.append(this)

    # Table Disk Status--need to fix last space column
    cnt = 0
    for x, val in enumerate(searchlines[diskidx:]):
        if '---' in val:
            cnt += 1
            if cnt == 2:
                diskstart = diskidx + x + 1
            if cnt == 3:
                diskfinal = diskidx + x
                break

    r = searchlines[diskstart: diskfinal]
    rows7 = list()
    found_table7 = True

    for line in r:
        if found_table7:
            this = [x.strip() for x in line.split("  ") if x != '']
            rows7.append(this)

    # Table Net Show Hardware
    cnt = 0
    for x, val in enumerate(searchlines[netidx:]):
        if '---' in val:
            cnt += 1
            if cnt == 2:
                netstart = netidx + x + 1
            if cnt == 3:
                netfinal = netidx + x
                break

    q = searchlines[netstart: netfinal]
    rows6 = list()
    found_table6 = True

    for line in q:
        if found_table6:
            this = [x.strip() for x in line.replace(
                "DA Copper", "Copper").split() if x != '']
            rows6.append(this)

    # Table Enclosure Show Summary
    cnt = 0
    for x, val in enumerate(searchlines[encidx:]):
        if '---' in val:
            cnt += 1
            if cnt == 2:
                encstart = encidx + x + 1
            if cnt == 3:
                encfinal = encidx + x
                break

    p = searchlines[encstart: encfinal]
    rows5 = list()
    found_table5 = True

    for line in p:
        if found_table5:
            this = [x.strip() for x in line.split() if x != '']
            rows5.append(this)

    # Table Feature Licenses
    cnt = 0
    for x, val in enumerate(searchlines[licidx:]):
        if '---' in val:
            cnt += 1
            if cnt == 1:
                licstart = licidx + x + 1
            if cnt == 2:
                licfinal = licidx + x
                break

    n = searchlines[licstart: licfinal]
    rows3 = list()
    found_table3 = True

    for line in n:
        if found_table3:
            this = [x.strip() for x in line.split() if x != '']
            rows3.append(this)

    cnt = 0
    # Table Mtree list
    for x, val in enumerate(searchlines[mtreeidx:]):
        if '---'in val:
            cnt += 1
            if cnt == 2:
                mtreestartidx = mtreeidx + x + 1
            if cnt == 3:
                mtreefinalidx = mtreeidx + x
                break

    m = searchlines[mtreestartidx: mtreefinalidx]
    rows2 = list()
    found_table2 = True

    for line in m:
        if found_table2:
            this = [x.strip() for x in line.split(" ") if x != '']
            rows2.append(this)

    # Creates dictionaries for requested data, used in the DF creation
    head_dict = {'Server_Usage': [
        'Resource', 'Size GiB', 'Used GiB', 'Avail GiB', 'Use%', 'Cleanable GiB']}
    head_dict2 = {'Mtree List': ['Mtrees', 'Pre GiB 24hrs', 'Post GiB 24hrs', 'Global Factor 24hrs', 'Local Factor 24hrs',
                                 'Total Factor 24hrs', 'Pre GiB 7days', 'Post GiB 7days', 'Global Factor 7days', 'Local Factor 7days', 'Total Factor 7Days']}
    head_dict3 = {'Feature licenses': [
        'Number', 'Feature', 'Count', 'Mode', 'Expiration Date']}
    head_dict4 = {'Capacity licenses': [
        'Number', 'Feature', 'Shelf Model', 'Capacity', 'Unit', 'Mode', 'Expiration Date']}
    head_dict5 = {'Enclosure Summary': [
        'Number', 'Model', 'Serial', 'State', 'Capacity', 'Type']}
    head_dict6 = {'Net Show': ['Port', 'Speed', 'Duplex', 'Supp Speeds',
                               'Hardware Address', 'Physical', 'Link Status', 'State']}
    head_dict7 = {'Disk Status': [
        'Disk States', 'Active Tier', 'Head Unit', 'Other', 'Cache Tier']}
    head_dict8 = {'Connections': ['Clients', 'Idle', 'CPUs',
                                  'Memory(MiB)', 'Plugin', 'OS Version', 'App Version', 'Encrypted', 'DSP', 'Transport']}
    head_dict9 = {'File Distribution': [
        'Age', 'Files', '%', 'Cumulative %', 'GiB', '%', 'Cumulative %']}

    # Creates the DF with the dictionaries
    df = pd.DataFrame(rows, columns=head_dict['Server_Usage'])
    df2 = pd.DataFrame(rows2, columns=head_dict2['Mtree List'])
    df3 = pd.DataFrame(rows3, columns=head_dict3['Feature licenses'])
    df4 = pd.DataFrame(rows4, columns=head_dict4['Capacity licenses'])
    df5 = pd.DataFrame(rows5, columns=head_dict5['Enclosure Summary'])
    df6 = pd.DataFrame(rows6, columns=head_dict6['Net Show'])
    df7 = pd.DataFrame(rows7, columns=head_dict7['Disk Status'])
    df8 = pd.DataFrame(rows8, columns=head_dict8['Connections'])
    df9 = pd.DataFrame(rows9, columns=head_dict9['File Distribution'])

    # Checks if the DF was created ok
    # df9

    # Writes the DFs to file in Excel
    writer = pd.ExcelWriter(r'uploads/output.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Table 1')
    df2.to_excel(writer, sheet_name='Table 2')
    writer.save()

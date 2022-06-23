import sys, os
import csv

def cleandict(infile, outfile):
    dictreader = csv.DictReader(open(infile))
    of = open(outfile, 'w')
    writer = csv.DictWriter(of, fieldnames = dictreader.fieldnames)
    writer.writeheader()
    for row in dictreader:
        newrow = row
        try:
            newrow['energy_source'] = row['energy_source'].replace(
                'grid_LUKU', 'electricity')
            newrow['mill_type'] = row['mill_type'].replace(
                'rolling', 'roller').replace(
                'rice_grinding_machine', 'rice_milling_machine').replace(
                'maize_germ_extractor', 'dehuller')

        except:
            print('not found')
        writer.writerow(newrow)


def clean(infile, outfile):
    reader = csv.reader(open(infile))
    data = list(reader)
    headers = data.pop(0)

    of = open(outfile, 'w')
    writer = csv.writer(of)

    for row in data:
        energy = ''
        if row[14].lower() == 'grid_luku':
            energy = 'Electricity'
        else:
            energy = row[14]
        newrow = []
        newrow.extend(row[0:14])
        newrow.append(energy)
        newrow.extend(row[14][15:])
        writer.writerow(newrow)

if __name__ == "__main__":
    indir = sys.argv[1]
    filelist = os.listdir(indir)
    outdir = os.path.join(indir,'CLEANED')
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    for filename in filelist:
        infile = os.path.join(indir, filename)
        (filepath, ext) = os.path.splitext(filename)
        outfile = os.path.join(outdir,filename)
        if ext == '.csv':
            try:
                cleandict(infile, outfile)
            except Exception as e:
                print('this file is fucked up')
                print(filename)
                print(e)

    #print(filelist)
    #clean(sys.argv[1])
    #newfilename = filepath + '_CLEANED' + ext
    #dirname = os.path.dirname(filename)
    # print(row['interviewee_mill_owner'])


    

import sys, os
import csv

def cleandict(infile, outfile):
    dictreader = csv.DictReader(open(infile))
    for row in dictreader:
        energy = ''
        mill_type = ''
        try:
            energy = row['energy_source'].replace(
                'grid_LUKU', 'electricity')
            mill_type = row['mill_type'].replace(
                'rolling', 'roller').replace(
                'rice_grinding_machine', 'rice_milling_machine').replace(
                'maize_germ_extractor', 'dehuller')

        except:
            print('not found')
        print(energy)
        print(mill_type)

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
        try:
            cleandict(infile, outfile)
        except:
            print('this file is fucked up')
            print(filename)

    #print(filelist)
    #clean(sys.argv[1])
    #newfilename = filepath + '_CLEANED' + ext
    #dirname = os.path.dirname(filename)
    # print(row['interviewee_mill_owner'])


    

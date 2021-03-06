#!/usr/bin/env python2

from argparse import ArgumentParser
from subprocess import Popen, PIPE
import os

def blast(input_query, dbs, proc, evalue, outformat, type):
    ##output_list = []
    for db in dbs:
        output_name = "d_{}_q_{}.txt".format(os.path.basename(db)[:-4],
                    os.path.basename(input_query)[:-4])
        blast_command = ["-query",
                        input_query,
                        "-db",
                        db,
                        "-outfmt",
                        outformat,
                        "-evalue",
                        evalue,
                        "-num_threads",
                        proc,
                        "-out",
                        output_name]
        if type == "prot":
            print "running cmd: {}\n".format(" ".join(["tblastn"]+blast_command))
            p = Popen(["tblastn"]+blast_command, stdout=PIPE, stderr=PIPE)
            p.wait()
            stdout, stderr = p.communicate()
            print stderr
        elif type == "nucl":
            print "Attempting to perform blastn instead"
            print "running cmd: {}\n".format(" ".join(["blastn"] +
                                                      blast_command))
            p = Popen(["blastn"] + blast_command, stdout=PIPE, stderr=PIPE)
            p.wait()
            stdout, stderr = p.communicate()
            print stderr
        else:
            print "wrong type of sequence given to -st option"

        ##output_list.append(output_name)
    ##return output_list

def main():
    parser = ArgumentParser(description = 'Performes blast searches from \
                                          protein and nucleotide queries \
                                          in several \
                                          nucleotide databases')
    parser.add_argument('-q','--query', dest = 'query', required = True,
                        nargs = '+', help = 'Provide input queries (fastas).')
    parser.add_argument('-d', '--database', dest = 'database', required =
    True , nargs = '+', help = 'Provide databases to make queries')
    parser.add_argument('-t', '--threads', dest='threads', default='1',
                        help='Provide the number of threads to use')
    parser.add_argument('-e', '--evalue', dest='evalue', default='0.000001',
                        help='Provide the evalue to use')
    # adds by default the default tabular output with two additional parameters
    # sacc - sequence accession and qlen - length of query
    parser.add_argument('-of', '--outfmt', dest='outfmt', default='6 qseqid '
                                                                  'sseqid '
                                                                  'pident '
                                                                  'length '
                                                                  'mismatch '
                                                                  'gapopen '
                                                                  'qstart '
                                                                  'qend '
                                                                  'sstart '
                                                                  'send '
                                                                  'evalue '
                                                                  'bitscore '
                                                                  'sacc '
                                                                  'qlen',
                        help='Provide the output format type')
    parser.add_argument('-st', '--sequence-type', dest='seq_type', choices=[
        'prot', 'nucl'], default='nucl', help='Indicate the sequence type')

    args = parser.parse_args()

    dbs = args.database
    query_search = args.query
    proc = args.threads
    evalue = args.evalue
    outformat = args.outfmt
    type = args.seq_type
    print type

    for search in query_search:
        blast(search, dbs, proc, evalue, outformat, type)

if __name__ == "__main__":
    main()
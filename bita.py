#!/usr/bin/env python2

from argparse import ArgumentParser
from subprocess import Popen, PIPE
import os

def blast(input_query, dbs, proc, evalue, outformat):
    ##output_list = []
    for db in dbs:
        stdout, stderr = "",""
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
        print "running cmd: {}\n".format(" ".join(["tblastn"]+blast_command))
        p = Popen(["tblastn"]+blast_command, stdout=PIPE, stderr=PIPE)
        p.wait()
        stdout, stderr = p.communicate()
        print stderr
        if stderr:
            print "Attempting to perform blastn instead"
            print "running cmd: {}\n".format(" ".join(["blastn"] +
                                                      blast_command))
            p = Popen(["blastn"] + blast_command, stdout=PIPE, stderr=PIPE)
            p.wait()
            stdout, stderr = p.communicate()
            print stderr

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
    parser.add_argument('-e', '--evalue', dest='evalue', default='1',
                        help='Provide the evalue to use')
    parser.add_argument('-of', '--outfmt', dest='outfmt', default='1',
                        help='Provide the outpoutput format type')

    args = parser.parse_args()

    dbs = args.database
    query_search = args.query
    proc = args.threads
    evalue = args.evalue
    outformat = args.outfmt

    for search in query_search:
        blast(search, dbs, proc, evalue, outformat)

if __name__ == "__main__":
    main()

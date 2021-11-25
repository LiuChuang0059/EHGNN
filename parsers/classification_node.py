import argparse

class Parser:

    def __init__(self):

        self.parser = argparse.ArgumentParser(description='HyperDrop')
        self.parser.add_argument('--type', type=str, required=True)

        self.set_arguments()

    def set_arguments(self):

        ### Experiment 
        self.parser.add_argument('--seed', type=int, default=42, help='seed')
        self.parser.add_argument("--gpu", type=int, default=-1)
        self.parser.add_argument('--experiment-number', default='001', type=str)

        ### Dataset

        self.parser.add_argument('--data', default='cora', type=str,
                            choices=['cora', 'citeseer'],
                            help='dataset type')

        ### Model
        self.parser.add_argument("--model", type=str, default='HyperDrop', choices=['HyperDrop'])
        self.parser.add_argument('--num-convs', default=2, type=int)
        self.parser.add_argument('--num-hidden', type=int, default=32, help='hidden size')
        self.parser.add_argument('--num-edge-hidden', type=int, default=16)
        self.parser.add_argument('--edge-ratio', type=float, default=0.8, help='pooling ratio for edges')

        ### Training
        self.parser.add_argument('--lr', type=float, default=0.01, help='learning rate')
        self.parser.add_argument('--weight-decay', type=float, default=5e-4, help='weight decay')
        self.parser.add_argument("--grad-norm", type=float, default=1.0)
        self.parser.add_argument("--dropout", type=float, default=0.5)
        self.parser.add_argument('--num-epochs', default=5000, type=int, help='train epochs number')
        self.parser.add_argument('--patience', type=int, default=300, help='patience for earlystopping')
        self.parser.add_argument("--lr-schedule", action='store_true')
        
    def parse(self):

        args, unparsed  = self.parser.parse_known_args()
        
        if len(unparsed) != 0:
            raise SystemExit('Unknown argument: {}'.format(unparsed))
        
        return args
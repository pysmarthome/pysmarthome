from pysmarhome_cli.request import request

def trigger_action(args):
    [id, action_id, *action_args] = args.action
    request(f'{args.host}/{id}', args.api_key, method='post', payload={
        'action': action_id,
        'args': action_args,
    })

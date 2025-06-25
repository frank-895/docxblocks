from .blocks import Block

def validate_blocks(data: list):
    return [Block.parse_obj(b) for b in data]
from const import UNIT_IN_BPS


def arbitrage_condition(
    x1: int, y1: int, x2: int, y2: int, r1_bps: int, r2_bps: int
) -> bool:
    """
    Check if arbitrage condition is satisfied for 2 Uniswapv2 type DEXes

    Args:
        x1 (int): reserve of x token on the 1st DEX
        y1 (int): reserve of y token on the 1st DEX
        x2 (int): reserve of x token on the 2nd DEX
        y2 (int): reserve of y token on the 2nd DEX
        r1_bps (int): 1 - phi1 in basis points, where phi1 is the fee for 1st DEX
        r2_bps (int): 1 - phi2 in basis points, where phi2 is the fee for 2nd DEX

    Returns:
        bool: Returns True if arbitrage opportunity exists and False otherwise
    """

    # YOUR CODE GOES HERE

    return False


def get_optimal_dx(x1: int, y1: int, x2: int, y2: int, r1_bps: int, r2_bps: int) -> int:
    """
    Calculate optimal dx for executing the arbitrage opportunity

    Args:
        x1 (int): reserve of x token on the 1st DEX
        y1 (int): reserve of y token on the 1st DEX
        x2 (int): reserve of x token on the 2nd DEX
        y2 (int): reserve of y token on the 2nd DEX
        r1_bps (int): 1 - phi1 in basis points, where phi1 is the fee for 1st DEX
        r2_bps (int): 1 - phi2 in basis points, where phi2 is the fee for 2nd DEX


    Returns:
        int: Arbitrage optimal dx for swapping dx -> dy -> dx'
    """

    # YOUR CODE GOES HERE

    return 0


def get_optimal_profit(
    x1: int, y1: int, x2: int, y2: int, r1_bps: int, r2_bps: int
) -> int:
    """
    Returns maximized profit from executing of the arbitrage opportunity

    Args:
        x1 (int): reserve of x token on the 1st DEX
        y1 (int): reserve of y token on the 1st DEX
        x2 (int): reserve of x token on the 2nd DEX
        y2 (int): reserve of y token on the 2nd DEX
        r1_bps (int): 1 - phi1 in basis points, where phi1 is the fee for 1st DEX
        r2_bps (int): 1 - phi2 in basis points, where phi2 is the fee for 2nd DEX

    Returns:
        int: Maximized profit from executing the arbitrage opportunity
    """

    # YOUR CODE GOES HERE

    return 0

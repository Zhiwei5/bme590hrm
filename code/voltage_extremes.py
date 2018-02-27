def voltage_extremes(x):
    """
    find the minimum and the maximum of a list of voltage and return a tuple

    :param x: the input should be a list
    :raises ImportError:  if the module not found
    :raises TypeError:  if the input is not a list or the input includes string
    :raises ValueError: if the input includes string

    :returns: return a tuple include minimum and maximum of the list
    :rtype: (float,float)
    """
    try:
        import logging
    except ImportError:
        print("Could not import logging module")
        return
    else:
        logging.basicConfig(filename='example.log', level=logging.DEBUG,
                            filemode='w')
    if type(x) is not list:
        logging.error('Watch out!The input should be list')
        raise TypeError('TypeError with the input')
    if not x:
        logging.warning("Empty list given")
        return (None, None)
    for val in x:
        try:
            num = float(val)
        except ValueError:
            logging.debug("Type is not able to be cast to float")
            raise ValueError()
        except TypeError as err:
            logging.debug("Erroneous type encountered: {}".format(type(err)))
            raise TypeError()
        else:
            if num == float('inf') or num == float('-inf'):
                raise ValueError()
    my_min = min(x)
    my_max = max(x)
    my_min_max = (my_min, my_max)
    logging.info("Returning min and max tuple")
    return my_min_max

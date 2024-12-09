"""
This file is intended to mask the AoN cython module to delay pyarrow imports
"""

def one_to_all(origin, matrix, graph, result, aux_result, curr_thread):
    from aequilibrae.paths.AoN import one_to_all as cython_one_to_all
    cython_one_to_all(origin, matrix, graph, result, aux_result, curr_thread)

def path_computation(origin, destination, graph, results):
    from aequilibrae.paths.AoN import path_computation as cython_path_computation
    cython_path_computation(origin, destination, graph, results)

def update_path_trace(results, destination, graph):
    from aequilibrae.paths.AoN import update_path_trace as cython_update_path_trace
    cython_update_path_trace(results, destination, graph)

def skimming_single_origin(origin, graph, result, aux_result, curr_thread):
    from aequilibrae.paths.AoN import skimming_single_origin as cython_skimming_single_origin
    cython_skimming_single_origin(origin, graph, result, aux_result, curr_thread)
from django.shortcuts import render
import random
import time
import statistics


# Create your views here.

def insertionsort(my_list):
    for i in range(1, len(my_list)):
        deger = my_list[i]
        j = i - 1
        while (j >= 0 and deger < my_list[j]):
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = deger
    return my_list

def bubblesort(my_list):
    for i in range(len(my_list) - 1):
        for j in range(0, len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


def quicksort(my_list):
    if len(my_list) <= 1:
        return my_list
    pivot = my_list[len(my_list) // 100]
    left = [x for x in my_list if x < pivot]
    middle = [x for x in my_list if x == pivot]
    right = [x for x in my_list if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def mergesort(my_list):
    if len(my_list) < 2:
        return my_list
    result = []
    mid = int(len(my_list) / 100)
    y = mergesort(my_list[:mid])
    z = mergesort(my_list[mid:])
    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z[0])
            z.pop(0)
        else:
            result.append(y[0])
            y.pop(0)
    result += y
    result += z
    return result


def yuz(request):
    insertion_sort_time_list = []
    insertion_sort_time_list_best = []
    insertion_sort_time_list_worst = []
    bubble_sort_time_list = []
    bubble_sort_time_list_best = []
    bubble_sort_time_list_worst = []
    quick_sort_time_list = []
    quick_sort_time_list_best = []
    quick_sort_time_list_worst = []
    merge_sort_time_list = []
    merge_sort_time_list_best = []
    merge_sort_time_list_worst = []

    # sayı üret
    my_list = []
    for s in range(100):
        for i in range(100):
            my_list.append(random.randint(1, 10000))
        my_list_sorted = sorted(my_list)
        my_list_sorted_rev = sorted(my_list, reverse=True)

        # starting time
        start = time.time()

        # insertion sort
        insertionsort(my_list)

        # end time
        end = time.time()

        insertion_sort_time = end - start
        insertion_sort_time_list.append(insertion_sort_time)

        # starting time
        start = time.time()

        # insertion sort best case
        insertionsort(my_list_sorted)

        # end time
        end = time.time()

        insertion_sort_time_best = end - start
        insertion_sort_time_list_best.append(insertion_sort_time_best)

        # starting time
        start = time.time()

        # insertion sort best case
        insertionsort(my_list_sorted_rev)

        # end time
        end = time.time()

        insertion_sort_time_worst = end - start
        insertion_sort_time_list_worst.append(insertion_sort_time_worst)

        # starting time
        start = time.time()

        # bubble sort
        bubblesort(my_list)

        # end time
        end = time.time()

        bubble_sort_time = end - start
        bubble_sort_time_list.append(bubble_sort_time)

        # starting time
        start = time.time()

        # bubble sort best case
        bubblesort(my_list_sorted)

        # end time
        end = time.time()

        bubble_sort_time_best = end - start
        bubble_sort_time_list_best.append(bubble_sort_time_best)

        # starting time worst case
        start = time.time()

        # bubble sort
        bubblesort(my_list_sorted_rev)

        # end time
        end = time.time()

        bubble_sort_time_worst = end - start
        bubble_sort_time_list_worst.append(bubble_sort_time_worst)

        # starting time
        start = time.time()

        # quick sort
        quicksort(my_list)

        # end time
        end = time.time()

        quick_sort_time = end - start
        quick_sort_time_list.append(quick_sort_time)

        # starting time
        start = time.time()

        # quick sort best case
        quicksort(my_list_sorted)

        # end time
        end = time.time()

        quick_sort_time_best = end - start
        quick_sort_time_list_best.append(quick_sort_time_best)

        # starting time
        start = time.time()

        # quick sort worst case
        quicksort(my_list_sorted_rev)

        # end time
        end = time.time()

        quick_sort_time_worst = end - start
        quick_sort_time_list_worst.append(quick_sort_time_worst)

        # starting time
        start = time.time()

        # merge sort
        mergesort(my_list)

        # end time
        end = time.time()

        merge_sort_time = end - start
        merge_sort_time_list.append(merge_sort_time)

        # starting time
        start = time.time()

        # merge sort best case
        mergesort(my_list_sorted)

        # end time
        end = time.time()

        merge_sort_time_best = end - start
        merge_sort_time_list_best.append(merge_sort_time_best)

        # starting time
        start = time.time()

        # merge sort worst case
        mergesort(my_list_sorted_rev)

        # end time
        end = time.time()

        merge_sort_time_worst = end - start
        merge_sort_time_list_worst.append(merge_sort_time_worst)

    insertion_sort_time_avg = sum(insertion_sort_time_list) / 100
    insertion_sort_time_best = sum(insertion_sort_time_list_best) / 100
    insertion_sort_time_worst = sum(insertion_sort_time_list_worst) / 100
    insertion_sort_time_stdev = statistics.stdev(insertion_sort_time_list)
    insertion_sort_time_min = min(insertion_sort_time_list)
    insertion_sort_time_max = max(insertion_sort_time_list)

    bubble_sort_time_avg = sum(bubble_sort_time_list) / 100
    bubble_sort_time_best = sum(bubble_sort_time_list_best) / 100
    bubble_sort_time_worst = sum(bubble_sort_time_list_worst) / 100
    bubble_sort_time_stdev = statistics.stdev(bubble_sort_time_list)
    bubble_sort_time_min = min(bubble_sort_time_list)
    bubble_sort_time_max = max(bubble_sort_time_list)

    quick_sort_time_avg = sum(quick_sort_time_list) / 100
    quick_sort_time_best = sum(quick_sort_time_list_best) / 100
    quick_sort_time_worst = sum(quick_sort_time_list_worst) / 100
    quick_sort_time_stdev = statistics.stdev(quick_sort_time_list)
    quick_sort_time_min = min(quick_sort_time_list)
    quick_sort_time_max = max(quick_sort_time_list)

    merge_sort_time_avg = sum(merge_sort_time_list) / 100
    merge_sort_time_best = sum(merge_sort_time_list_best) / 100
    merge_sort_time_worst = sum(merge_sort_time_list_worst) / 100
    merge_sort_time_stdev = statistics.stdev(merge_sort_time_list)
    merge_sort_time_min = min(merge_sort_time_list)
    merge_sort_time_max = max(merge_sort_time_list)

    context = {
        "insertion_sort_time_avg": insertion_sort_time_avg,
        "insertion_sort_time_stdev": insertion_sort_time_stdev,
        "insertion_sort_time_min": insertion_sort_time_min,
        "insertion_sort_time_max": insertion_sort_time_max,
        "insertion_sort_time_best": insertion_sort_time_best,
        "insertion_sort_time_worst": insertion_sort_time_worst,
        "bubble_sort_time_avg": bubble_sort_time_avg,
        "bubble_sort_time_stdev": bubble_sort_time_stdev,
        "bubble_sort_time_min": bubble_sort_time_min,
        "bubble_sort_time_max": bubble_sort_time_max,
        "bubble_sort_time_best": bubble_sort_time_best,
        "bubble_sort_time_worst": bubble_sort_time_worst,
        "quick_sort_time_avg": quick_sort_time_avg,
        "quick_sort_time_stdev": quick_sort_time_stdev,
        "quick_sort_time_min": quick_sort_time_min,
        "quick_sort_time_max": quick_sort_time_max,
        "quick_sort_time_best": quick_sort_time_best,
        "quick_sort_time_worst": quick_sort_time_worst,
        "merge_sort_time_avg": merge_sort_time_avg,
        "merge_sort_time_stdev": merge_sort_time_stdev,
        "merge_sort_time_min": merge_sort_time_min,
        "merge_sort_time_max": merge_sort_time_max,
        "merge_sort_time_best": merge_sort_time_best,
        "merge_sort_time_worst": merge_sort_time_worst,
    }
    return render(request, 'yuz.html', context)


def besyuz(request):
    insertion_sort_time_list = []
    insertion_sort_time_list_best = []
    insertion_sort_time_list_worst = []
    bubble_sort_time_list = []
    bubble_sort_time_list_best = []
    bubble_sort_time_list_worst = []
    quick_sort_time_list = []
    quick_sort_time_list_best = []
    quick_sort_time_list_worst = []
    merge_sort_time_list = []
    merge_sort_time_list_best = []
    merge_sort_time_list_worst = []

    # sayı üret
    my_list = []
    for s in range(100):
        for i in range(500):
            my_list.append(random.randint(1, 10000))
        my_list_sorted = sorted(my_list)
        my_list_sorted_rev = sorted(my_list, reverse=True)

        # starting time
        start = time.time()

        # insertion sort
        insertionsort(my_list)

        # end time
        end = time.time()

        insertion_sort_time = end - start
        insertion_sort_time_list.append(insertion_sort_time)

        # starting time
        start = time.time()

        # insertion sort best case
        insertionsort(my_list_sorted)

        # end time
        end = time.time()

        insertion_sort_time_best = end - start
        insertion_sort_time_list_best.append(insertion_sort_time_best)

        # starting time
        start = time.time()

        # insertion sort best case
        insertionsort(my_list_sorted_rev)

        # end time
        end = time.time()

        insertion_sort_time_worst = end - start
        insertion_sort_time_list_worst.append(insertion_sort_time_worst)

        # starting time
        start = time.time()

        # bubble sort
        bubblesort(my_list)

        # end time
        end = time.time()

        bubble_sort_time = end - start
        bubble_sort_time_list.append(bubble_sort_time)

        # starting time
        start = time.time()

        # bubble sort best case
        bubblesort(my_list_sorted)

        # end time
        end = time.time()

        bubble_sort_time_best = end - start
        bubble_sort_time_list_best.append(bubble_sort_time_best)

        # starting time worst case
        start = time.time()

        # bubble sort
        bubblesort(my_list_sorted_rev)

        # end time
        end = time.time()

        bubble_sort_time_worst = end - start
        bubble_sort_time_list_worst.append(bubble_sort_time_worst)

        # starting time
        start = time.time()

        # quick sort
        quicksort(my_list)

        # end time
        end = time.time()

        quick_sort_time = end - start
        quick_sort_time_list.append(quick_sort_time)

        # starting time
        start = time.time()

        # quick sort best case
        quicksort(my_list_sorted)

        # end time
        end = time.time()

        quick_sort_time_best = end - start
        quick_sort_time_list_best.append(quick_sort_time_best)

        # starting time
        start = time.time()

        # quick sort worst case
        quicksort(my_list_sorted_rev)

        # end time
        end = time.time()

        quick_sort_time_worst = end - start
        quick_sort_time_list_worst.append(quick_sort_time_worst)

        # starting time
        start = time.time()

        # merge sort
        mergesort(my_list)

        # end time
        end = time.time()

        merge_sort_time = end - start
        merge_sort_time_list.append(merge_sort_time)

        # starting time
        start = time.time()

        # merge sort best case
        mergesort(my_list_sorted)

        # end time
        end = time.time()

        merge_sort_time_best = end - start
        merge_sort_time_list_best.append(merge_sort_time_best)

        # starting time
        start = time.time()

        # merge sort worst case
        mergesort(my_list_sorted_rev)

        # end time
        end = time.time()

        merge_sort_time_worst = end - start
        merge_sort_time_list_worst.append(merge_sort_time_worst)

    insertion_sort_time_avg = sum(insertion_sort_time_list) / 100
    insertion_sort_time_best = sum(insertion_sort_time_list_best) / 100
    insertion_sort_time_worst = sum(insertion_sort_time_list_worst) / 100
    insertion_sort_time_stdev = statistics.stdev(insertion_sort_time_list)
    insertion_sort_time_min = min(insertion_sort_time_list)
    insertion_sort_time_max = max(insertion_sort_time_list)

    bubble_sort_time_avg = sum(bubble_sort_time_list) / 100
    bubble_sort_time_best = sum(bubble_sort_time_list_best) / 100
    bubble_sort_time_worst = sum(bubble_sort_time_list_worst) / 100
    bubble_sort_time_stdev = statistics.stdev(bubble_sort_time_list)
    bubble_sort_time_min = min(bubble_sort_time_list)
    bubble_sort_time_max = max(bubble_sort_time_list)

    quick_sort_time_avg = sum(quick_sort_time_list) / 100
    quick_sort_time_best = sum(quick_sort_time_list_best) / 100
    quick_sort_time_worst = sum(quick_sort_time_list_worst) / 100
    quick_sort_time_stdev = statistics.stdev(quick_sort_time_list)
    quick_sort_time_min = min(quick_sort_time_list)
    quick_sort_time_max = max(quick_sort_time_list)

    merge_sort_time_avg = sum(merge_sort_time_list) / 100
    merge_sort_time_best = sum(merge_sort_time_list_best) / 100
    merge_sort_time_worst = sum(merge_sort_time_list_worst) / 100
    merge_sort_time_stdev = statistics.stdev(merge_sort_time_list)
    merge_sort_time_min = min(merge_sort_time_list)
    merge_sort_time_max = max(merge_sort_time_list)

    context = {
        "insertion_sort_time_avg": insertion_sort_time_avg,
        "insertion_sort_time_stdev": insertion_sort_time_stdev,
        "insertion_sort_time_min": insertion_sort_time_min,
        "insertion_sort_time_max": insertion_sort_time_max,
        "insertion_sort_time_best": insertion_sort_time_best,
        "insertion_sort_time_worst": insertion_sort_time_worst,
        "bubble_sort_time_avg": bubble_sort_time_avg,
        "bubble_sort_time_stdev": bubble_sort_time_stdev,
        "bubble_sort_time_min": bubble_sort_time_min,
        "bubble_sort_time_max": bubble_sort_time_max,
        "bubble_sort_time_best": bubble_sort_time_best,
        "bubble_sort_time_worst": bubble_sort_time_worst,
        "quick_sort_time_avg": quick_sort_time_avg,
        "quick_sort_time_stdev": quick_sort_time_stdev,
        "quick_sort_time_min": quick_sort_time_min,
        "quick_sort_time_max": quick_sort_time_max,
        "quick_sort_time_best": quick_sort_time_best,
        "quick_sort_time_worst": quick_sort_time_worst,
        "merge_sort_time_avg": merge_sort_time_avg,
        "merge_sort_time_stdev": merge_sort_time_stdev,
        "merge_sort_time_min": merge_sort_time_min,
        "merge_sort_time_max": merge_sort_time_max,
        "merge_sort_time_best": merge_sort_time_best,
        "merge_sort_time_worst": merge_sort_time_worst,
    }
    return render(request, 'besyuz.html', context)


def bin(request):
    insertion_sort_time_list = []
    insertion_sort_time_list_best = []
    insertion_sort_time_list_worst = []
    bubble_sort_time_list = []
    bubble_sort_time_list_best = []
    bubble_sort_time_list_worst = []
    quick_sort_time_list = []
    quick_sort_time_list_best = []
    quick_sort_time_list_worst = []
    merge_sort_time_list = []
    merge_sort_time_list_best = []
    merge_sort_time_list_worst = []

    # sayı üret
    my_list = []
    for s in range(100):
        for i in range(1000):
            my_list.append(random.randint(1, 10000))
        my_list_sorted = sorted(my_list)
        my_list_sorted_rev = sorted(my_list, reverse=True)

        # starting time
        start = time.time()

        # insertion sort
        insertionsort(my_list)

        # end time
        end = time.time()

        insertion_sort_time = end - start
        insertion_sort_time_list.append(insertion_sort_time)

        # starting time
        start = time.time()

        # insertion sort best case
        insertionsort(my_list_sorted)

        # end time
        end = time.time()

        insertion_sort_time_best = end - start
        insertion_sort_time_list_best.append(insertion_sort_time_best)

        # starting time
        start = time.time()

        # insertion sort best case
        insertionsort(my_list_sorted_rev)

        # end time
        end = time.time()

        insertion_sort_time_worst = end - start
        insertion_sort_time_list_worst.append(insertion_sort_time_worst)

        # starting time
        start = time.time()

        # bubble sort
        bubblesort(my_list)

        # end time
        end = time.time()

        bubble_sort_time = end - start
        bubble_sort_time_list.append(bubble_sort_time)

        # starting time
        start = time.time()

        # bubble sort best case
        bubblesort(my_list_sorted)

        # end time
        end = time.time()

        bubble_sort_time_best = end - start
        bubble_sort_time_list_best.append(bubble_sort_time_best)

        # starting time worst case
        start = time.time()

        # bubble sort
        bubblesort(my_list_sorted_rev)

        # end time
        end = time.time()

        bubble_sort_time_worst = end - start
        bubble_sort_time_list_worst.append(bubble_sort_time_worst)

        # starting time
        start = time.time()

        # quick sort
        quicksort(my_list)

        # end time
        end = time.time()

        quick_sort_time = end - start
        quick_sort_time_list.append(quick_sort_time)

        # starting time
        start = time.time()

        # quick sort best case
        quicksort(my_list_sorted)

        # end time
        end = time.time()

        quick_sort_time_best = end - start
        quick_sort_time_list_best.append(quick_sort_time_best)

        # starting time
        start = time.time()

        # quick sort worst case
        quicksort(my_list_sorted_rev)

        # end time
        end = time.time()

        quick_sort_time_worst = end - start
        quick_sort_time_list_worst.append(quick_sort_time_worst)

        # starting time
        start = time.time()

        # merge sort
        mergesort(my_list)

        # end time
        end = time.time()

        merge_sort_time = end - start
        merge_sort_time_list.append(merge_sort_time)

        # starting time
        start = time.time()

        # merge sort best case
        mergesort(my_list_sorted)

        # end time
        end = time.time()

        merge_sort_time_best = end - start
        merge_sort_time_list_best.append(merge_sort_time_best)

        # starting time
        start = time.time()

        # merge sort worst case
        mergesort(my_list_sorted_rev)

        # end time
        end = time.time()

        merge_sort_time_worst = end - start
        merge_sort_time_list_worst.append(merge_sort_time_worst)

    insertion_sort_time_avg = sum(insertion_sort_time_list) / 100
    insertion_sort_time_best = sum(insertion_sort_time_list_best) / 100
    insertion_sort_time_worst = sum(insertion_sort_time_list_worst) / 100
    insertion_sort_time_stdev = statistics.stdev(insertion_sort_time_list)
    insertion_sort_time_min = min(insertion_sort_time_list)
    insertion_sort_time_max = max(insertion_sort_time_list)

    bubble_sort_time_avg = sum(bubble_sort_time_list) / 100
    bubble_sort_time_best = sum(bubble_sort_time_list_best) / 100
    bubble_sort_time_worst = sum(bubble_sort_time_list_worst) / 100
    bubble_sort_time_stdev = statistics.stdev(bubble_sort_time_list)
    bubble_sort_time_min = min(bubble_sort_time_list)
    bubble_sort_time_max = max(bubble_sort_time_list)

    quick_sort_time_avg = sum(quick_sort_time_list) / 100
    quick_sort_time_best = sum(quick_sort_time_list_best) / 100
    quick_sort_time_worst = sum(quick_sort_time_list_worst) / 100
    quick_sort_time_stdev = statistics.stdev(quick_sort_time_list)
    quick_sort_time_min = min(quick_sort_time_list)
    quick_sort_time_max = max(quick_sort_time_list)

    merge_sort_time_avg = sum(merge_sort_time_list) / 100
    merge_sort_time_best = sum(merge_sort_time_list_best) / 100
    merge_sort_time_worst = sum(merge_sort_time_list_worst) / 100
    merge_sort_time_stdev = statistics.stdev(merge_sort_time_list)
    merge_sort_time_min = min(merge_sort_time_list)
    merge_sort_time_max = max(merge_sort_time_list)

    context = {
        "insertion_sort_time_avg": insertion_sort_time_avg,
        "insertion_sort_time_stdev": insertion_sort_time_stdev,
        "insertion_sort_time_min": insertion_sort_time_min,
        "insertion_sort_time_max": insertion_sort_time_max,
        "insertion_sort_time_best": insertion_sort_time_best,
        "insertion_sort_time_worst": insertion_sort_time_worst,
        "bubble_sort_time_avg": bubble_sort_time_avg,
        "bubble_sort_time_stdev": bubble_sort_time_stdev,
        "bubble_sort_time_min": bubble_sort_time_min,
        "bubble_sort_time_max": bubble_sort_time_max,
        "bubble_sort_time_best": bubble_sort_time_best,
        "bubble_sort_time_worst": bubble_sort_time_worst,
        "quick_sort_time_avg": quick_sort_time_avg,
        "quick_sort_time_stdev": quick_sort_time_stdev,
        "quick_sort_time_min": quick_sort_time_min,
        "quick_sort_time_max": quick_sort_time_max,
        "quick_sort_time_best": quick_sort_time_best,
        "quick_sort_time_worst": quick_sort_time_worst,
        "merge_sort_time_avg": merge_sort_time_avg,
        "merge_sort_time_stdev": merge_sort_time_stdev,
        "merge_sort_time_min": merge_sort_time_min,
        "merge_sort_time_max": merge_sort_time_max,
        "merge_sort_time_best": merge_sort_time_best,
        "merge_sort_time_worst": merge_sort_time_worst,
    }
    return render(request, 'bin.html', context)


def besbin(request):
    insertion_sort_time_list = []
    insertion_sort_time_list_best = []
    insertion_sort_time_list_worst = []
    bubble_sort_time_list = []
    bubble_sort_time_list_best = []
    bubble_sort_time_list_worst = []
    quick_sort_time_list = []
    quick_sort_time_list_best = []
    quick_sort_time_list_worst = []
    merge_sort_time_list = []
    merge_sort_time_list_best = []
    merge_sort_time_list_worst = []

    # sayı üret
    my_list = []
    for s in range(100):
        for i in range(5000):
            my_list.append(random.randint(1, 10000))
        my_list_sorted = sorted(my_list)
        my_list_sorted_rev = sorted(my_list, reverse=True)

        # starting time
        start = time.time()

        # insertion sort
        insertionsort(my_list)

        # end time
        end = time.time()

        insertion_sort_time = end - start
        insertion_sort_time_list.append(insertion_sort_time)

        # starting time
        start = time.time()

        # insertion sort best case
        insertionsort(my_list_sorted)

        # end time
        end = time.time()

        insertion_sort_time_best = end - start
        insertion_sort_time_list_best.append(insertion_sort_time_best)

        # starting time
        start = time.time()

        # insertion sort best case
        insertionsort(my_list_sorted_rev)

        # end time
        end = time.time()

        insertion_sort_time_worst = end - start
        insertion_sort_time_list_worst.append(insertion_sort_time_worst)

        # starting time
        start = time.time()

        # bubble sort
        bubblesort(my_list)

        # end time
        end = time.time()

        bubble_sort_time = end - start
        bubble_sort_time_list.append(bubble_sort_time)

        # starting time
        start = time.time()

        # bubble sort best case
        bubblesort(my_list_sorted)

        # end time
        end = time.time()

        bubble_sort_time_best = end - start
        bubble_sort_time_list_best.append(bubble_sort_time_best)

        # starting time worst case
        start = time.time()

        # bubble sort
        bubblesort(my_list_sorted_rev)

        # end time
        end = time.time()

        bubble_sort_time_worst = end - start
        bubble_sort_time_list_worst.append(bubble_sort_time_worst)

        # starting time
        start = time.time()

        # quick sort
        quicksort(my_list)

        # end time
        end = time.time()

        quick_sort_time = end - start
        quick_sort_time_list.append(quick_sort_time)

        # starting time
        start = time.time()

        # quick sort best case
        quicksort(my_list_sorted)

        # end time
        end = time.time()

        quick_sort_time_best = end - start
        quick_sort_time_list_best.append(quick_sort_time_best)

        # starting time
        start = time.time()

        # quick sort worst case
        quicksort(my_list_sorted_rev)

        # end time
        end = time.time()

        quick_sort_time_worst = end - start
        quick_sort_time_list_worst.append(quick_sort_time_worst)

        # starting time
        start = time.time()

        # merge sort
        mergesort(my_list)

        # end time
        end = time.time()

        merge_sort_time = end - start
        merge_sort_time_list.append(merge_sort_time)

        # starting time
        start = time.time()

        # merge sort best case
        mergesort(my_list_sorted)

        # end time
        end = time.time()

        merge_sort_time_best = end - start
        merge_sort_time_list_best.append(merge_sort_time_best)

        # starting time
        start = time.time()

        # merge sort worst case
        mergesort(my_list_sorted_rev)

        # end time
        end = time.time()

        merge_sort_time_worst = end - start
        merge_sort_time_list_worst.append(merge_sort_time_worst)

    insertion_sort_time_avg = sum(insertion_sort_time_list) / 100
    insertion_sort_time_best = sum(insertion_sort_time_list_best) / 100
    insertion_sort_time_worst = sum(insertion_sort_time_list_worst) / 100
    insertion_sort_time_stdev = statistics.stdev(insertion_sort_time_list)
    insertion_sort_time_min = min(insertion_sort_time_list)
    insertion_sort_time_max = max(insertion_sort_time_list)

    bubble_sort_time_avg = sum(bubble_sort_time_list) / 100
    bubble_sort_time_best = sum(bubble_sort_time_list_best) / 100
    bubble_sort_time_worst = sum(bubble_sort_time_list_worst) / 100
    bubble_sort_time_stdev = statistics.stdev(bubble_sort_time_list)
    bubble_sort_time_min = min(bubble_sort_time_list)
    bubble_sort_time_max = max(bubble_sort_time_list)

    quick_sort_time_avg = sum(quick_sort_time_list) / 100
    quick_sort_time_best = sum(quick_sort_time_list_best) / 100
    quick_sort_time_worst = sum(quick_sort_time_list_worst) / 100
    quick_sort_time_stdev = statistics.stdev(quick_sort_time_list)
    quick_sort_time_min = min(quick_sort_time_list)
    quick_sort_time_max = max(quick_sort_time_list)

    merge_sort_time_avg = sum(merge_sort_time_list) / 100
    merge_sort_time_best = sum(merge_sort_time_list_best) / 100
    merge_sort_time_worst = sum(merge_sort_time_list_worst) / 100
    merge_sort_time_stdev = statistics.stdev(merge_sort_time_list)
    merge_sort_time_min = min(merge_sort_time_list)
    merge_sort_time_max = max(merge_sort_time_list)

    context = {
        "insertion_sort_time_avg": insertion_sort_time_avg,
        "insertion_sort_time_stdev": insertion_sort_time_stdev,
        "insertion_sort_time_min": insertion_sort_time_min,
        "insertion_sort_time_max": insertion_sort_time_max,
        "insertion_sort_time_best": insertion_sort_time_best,
        "insertion_sort_time_worst": insertion_sort_time_worst,
        "bubble_sort_time_avg": bubble_sort_time_avg,
        "bubble_sort_time_stdev": bubble_sort_time_stdev,
        "bubble_sort_time_min": bubble_sort_time_min,
        "bubble_sort_time_max": bubble_sort_time_max,
        "bubble_sort_time_best": bubble_sort_time_best,
        "bubble_sort_time_worst": bubble_sort_time_worst,
        "quick_sort_time_avg": quick_sort_time_avg,
        "quick_sort_time_stdev": quick_sort_time_stdev,
        "quick_sort_time_min": quick_sort_time_min,
        "quick_sort_time_max": quick_sort_time_max,
        "quick_sort_time_best": quick_sort_time_best,
        "quick_sort_time_worst": quick_sort_time_worst,
        "merge_sort_time_avg": merge_sort_time_avg,
        "merge_sort_time_stdev": merge_sort_time_stdev,
        "merge_sort_time_min": merge_sort_time_min,
        "merge_sort_time_max": merge_sort_time_max,
        "merge_sort_time_best": merge_sort_time_best,
        "merge_sort_time_worst": merge_sort_time_worst,
    }
    return render(request, 'besbin.html', context)


def onbin(request):
    insertion_sort_time_list = []
    insertion_sort_time_list_best = []
    insertion_sort_time_list_worst = []
    bubble_sort_time_list = []
    bubble_sort_time_list_best = []
    bubble_sort_time_list_worst = []
    quick_sort_time_list = []
    quick_sort_time_list_best = []
    quick_sort_time_list_worst = []
    merge_sort_time_list = []
    merge_sort_time_list_best = []
    merge_sort_time_list_worst = []

    # sayı üret
    my_list = []
    for s in range(100):
        for i in range(10000):
            my_list.append(random.randint(1, 10000))
        my_list_sorted = sorted(my_list)
        my_list_sorted_rev = sorted(my_list, reverse=True)

        # starting time
        start = time.time()

        # insertion sort
        insertionsort(my_list)

        # end time
        end = time.time()

        insertion_sort_time = end - start
        insertion_sort_time_list.append(insertion_sort_time)

        # starting time
        start = time.time()

        # insertion sort best case
        insertionsort(my_list_sorted)

        # end time
        end = time.time()

        insertion_sort_time_best = end - start
        insertion_sort_time_list_best.append(insertion_sort_time_best)

        # starting time
        start = time.time()

        # insertion sort best case
        insertionsort(my_list_sorted_rev)

        # end time
        end = time.time()

        insertion_sort_time_worst = end - start
        insertion_sort_time_list_worst.append(insertion_sort_time_worst)

        # starting time
        start = time.time()

        # bubble sort
        bubblesort(my_list)

        # end time
        end = time.time()

        bubble_sort_time = end - start
        bubble_sort_time_list.append(bubble_sort_time)

        # starting time
        start = time.time()

        # bubble sort best case
        bubblesort(my_list_sorted)

        # end time
        end = time.time()

        bubble_sort_time_best = end - start
        bubble_sort_time_list_best.append(bubble_sort_time_best)

        # starting time worst case
        start = time.time()

        # bubble sort
        bubblesort(my_list_sorted_rev)

        # end time
        end = time.time()

        bubble_sort_time_worst = end - start
        bubble_sort_time_list_worst.append(bubble_sort_time_worst)

        # starting time
        start = time.time()

        # quick sort
        quicksort(my_list)

        # end time
        end = time.time()

        quick_sort_time = end - start
        quick_sort_time_list.append(quick_sort_time)

        # starting time
        start = time.time()

        # quick sort best case
        quicksort(my_list_sorted)

        # end time
        end = time.time()

        quick_sort_time_best = end - start
        quick_sort_time_list_best.append(quick_sort_time_best)

        # starting time
        start = time.time()

        # quick sort worst case
        quicksort(my_list_sorted_rev)

        # end time
        end = time.time()

        quick_sort_time_worst = end - start
        quick_sort_time_list_worst.append(quick_sort_time_worst)

        # starting time
        start = time.time()

        # merge sort
        mergesort(my_list)

        # end time
        end = time.time()

        merge_sort_time = end - start
        merge_sort_time_list.append(merge_sort_time)

        # starting time
        start = time.time()

        # merge sort best case
        mergesort(my_list_sorted)

        # end time
        end = time.time()

        merge_sort_time_best = end - start
        merge_sort_time_list_best.append(merge_sort_time_best)

        # starting time
        start = time.time()

        # merge sort worst case
        mergesort(my_list_sorted_rev)

        # end time
        end = time.time()

        merge_sort_time_worst = end - start
        merge_sort_time_list_worst.append(merge_sort_time_worst)

    insertion_sort_time_avg = sum(insertion_sort_time_list) / 100
    insertion_sort_time_best = sum(insertion_sort_time_list_best) / 100
    insertion_sort_time_worst = sum(insertion_sort_time_list_worst) / 100
    insertion_sort_time_stdev = statistics.stdev(insertion_sort_time_list)
    insertion_sort_time_min = min(insertion_sort_time_list)
    insertion_sort_time_max = max(insertion_sort_time_list)

    bubble_sort_time_avg = sum(bubble_sort_time_list) / 100
    bubble_sort_time_best = sum(bubble_sort_time_list_best) / 100
    bubble_sort_time_worst = sum(bubble_sort_time_list_worst) / 100
    bubble_sort_time_stdev = statistics.stdev(bubble_sort_time_list)
    bubble_sort_time_min = min(bubble_sort_time_list)
    bubble_sort_time_max = max(bubble_sort_time_list)

    quick_sort_time_avg = sum(quick_sort_time_list) / 100
    quick_sort_time_best = sum(quick_sort_time_list_best) / 100
    quick_sort_time_worst = sum(quick_sort_time_list_worst) / 100
    quick_sort_time_stdev = statistics.stdev(quick_sort_time_list)
    quick_sort_time_min = min(quick_sort_time_list)
    quick_sort_time_max = max(quick_sort_time_list)

    merge_sort_time_avg = sum(merge_sort_time_list) / 100
    merge_sort_time_best = sum(merge_sort_time_list_best) / 100
    merge_sort_time_worst = sum(merge_sort_time_list_worst) / 100
    merge_sort_time_stdev = statistics.stdev(merge_sort_time_list)
    merge_sort_time_min = min(merge_sort_time_list)
    merge_sort_time_max = max(merge_sort_time_list)

    context = {
        "insertion_sort_time_avg": insertion_sort_time_avg,
        "insertion_sort_time_stdev": insertion_sort_time_stdev,
        "insertion_sort_time_min": insertion_sort_time_min,
        "insertion_sort_time_max": insertion_sort_time_max,
        "insertion_sort_time_best": insertion_sort_time_best,
        "insertion_sort_time_worst": insertion_sort_time_worst,
        "bubble_sort_time_avg": bubble_sort_time_avg,
        "bubble_sort_time_stdev": bubble_sort_time_stdev,
        "bubble_sort_time_min": bubble_sort_time_min,
        "bubble_sort_time_max": bubble_sort_time_max,
        "bubble_sort_time_best": bubble_sort_time_best,
        "bubble_sort_time_worst": bubble_sort_time_worst,
        "quick_sort_time_avg": quick_sort_time_avg,
        "quick_sort_time_stdev": quick_sort_time_stdev,
        "quick_sort_time_min": quick_sort_time_min,
        "quick_sort_time_max": quick_sort_time_max,
        "quick_sort_time_best": quick_sort_time_best,
        "quick_sort_time_worst": quick_sort_time_worst,
        "merge_sort_time_avg": merge_sort_time_avg,
        "merge_sort_time_stdev": merge_sort_time_stdev,
        "merge_sort_time_min": merge_sort_time_min,
        "merge_sort_time_max": merge_sort_time_max,
        "merge_sort_time_best": merge_sort_time_best,
        "merge_sort_time_worst": merge_sort_time_worst,
    }
    return render(request, 'onbin.html', context)

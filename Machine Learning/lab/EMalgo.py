# Apply EM algorithm to cluster a set of data stored in a .CSV file. Use the same data set for clustering using k-Means algorithm. Compare the results of these two algorithms and comment on the quality of clustering. You can add Java/Python ML library classes/API in the program.

import csv
import random
import math
import copy

# Read data from CSV file
def readData(filename):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for i in range(len(dataset)):
            dataset[i] = [float(x) for x in dataset[i]]
    return dataset

# Initialize the cluster centers
def initializeCenters(dataset, k):
    centers = []
    for i in range(k):
        centers.append(dataset[i])
    return centers

# Calculate Euclidean distance
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

# Assign data points to clusters
def assignClusters(dataset, centers):
    clusters = []
    for i in range(len(centers)):
        clusters.append([])
    for i in range(len(dataset)):
        distances = []
        for j in range(len(centers)):
            distances.append(euclideanDistance(dataset[i], centers[j], len(dataset[i])))
        cluster = distances.index(min(distances))
        clusters[cluster].append(dataset[i])
    return clusters

# Calculate new cluster centers
def calculateCenters(clusters):
    centers = []
    for i in range(len(clusters)):
        center = [0] * len(clusters[i][0])
        for j in range(len(clusters[i])):
            for k in range(len(clusters[i][j])):
                center[k] += clusters[i][j][k]
        for j in range(len(center)):
            center[j] /= len(clusters[i])
        centers.append(center)
    return centers

# Calculate the total distance between data points and their cluster centers
def calculateDistance(clusters, centers):
    distance = 0
    for i in range(len(clusters)):
        for j in range(len(clusters[i])):
            distance += euclideanDistance(clusters[i][j], centers[i], len(clusters[i][j]))
    return distance

# Apply EM algorithm
def EM(dataset, k):
    centers = initializeCenters(dataset, k)
    clusters = assignClusters(dataset, centers)
    oldDistance = 0
    newDistance = calculateDistance(clusters, centers)
    while newDistance != oldDistance:
        oldDistance = newDistance
        centers = calculateCenters(clusters)
        clusters = assignClusters(dataset, centers)
        newDistance = calculateDistance(clusters, centers)
    return clusters

# Apply k-Means algorithm
def kMeans(dataset, k):
    centers = initializeCenters(dataset, k)
    clusters = assignClusters(dataset, centers)
    oldCenters = []
    while oldCenters != centers:
        oldCenters = copy.deepcopy(centers)
        centers = calculateCenters(clusters)
        clusters = assignClusters(dataset, centers)
    return clusters

# Main
def main():
    filename = 'data.csv'
    dataset = readData(filename)
    k = 3
    EMclusters = EM(dataset, k)
    kMeansclusters = kMeans(dataset, k)
    print('EM Clusters:')
    print(EMclusters)
    print('k-Means Clusters:')
    print(kMeansclusters)

if __name__ == '__main__':
    main()

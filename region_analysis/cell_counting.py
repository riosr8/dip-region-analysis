import cv2
import numpy as np


class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        regions = dict()
        region_num_counter = 1
        r = np.zeros(image.shape, np.uint32)

        for (i, j), val in np.ndenumerate(image):
            if val == 255:
                if i == 10 and j == 193:
                    print(i)
                if i - 1 >= 0 and j - 1 >= 0:
                    if image[i, j - 1] == 0 and image[i - 1, j] == 0:
                        r[i, j] = region_num_counter
                        region_num_counter += 1
                    if image[i, j - 1] == 0 and image[i - 1, j] == 255:
                        r[i, j] = r[i - 1, j]
                    if image[i, j - 1] == 255 and image[i - 1, j] == 0:
                        r[i, j] = r[i, j - 1]

                    if image[i, j - 1] == 255 and image[i - 1, j] == 255:
                        r[i, j] = r[i-1, j]
                        r[i, j-1] = r[i-1, j]
                        d = 2
                        flag = 0
                        while flag == 0:
                            if image[i, j - d] != 0:
                                r[i, j-d] = r[i, j - d + 1]
                                d += 1
                            else:
                                flag = 1

                if i == 0 and j > 0:
                    if image[i, j - 1] == 0:
                        r[i, j] = region_num_counter
                        region_num_counter += 1
                    if image[i, j - 1] == 255:
                        r[i, j] = r[i, j - 1]

                if j == 0 and i > 0:
                    if image[i - 1, j] == 255:
                        r[i, j] = r[i - 1, j]
                    if image[i - 1, j] == 0:
                        r[i, j] = region_num_counter
                        region_num_counter += 1

        for (i, j), val in np.ndenumerate(image):
            if r[i, j] != 0:
                if r[i, j] in regions:
                    regions[r[i, j]].append([i, j])
                else:
                    regions[r[i, j]] = [[i, j]]

        return regions

    def compute_statistics(self, regions):
        """Compute cell statistics area and location
        takes as input
        region: a list of pixels in a region
        returns: area"""

        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        reduced_regions = {k: v for k, v in regions.items() if len(v) >= 15}

        stats = {}
        for region, points in reduced_regions.items():
            centroid = np.array(points).mean(axis=0)
            centroid = (centroid[0].round(), centroid[1].round())
            stats[region] = ((int(centroid[0]), int(centroid[1])), len(points))
            print(str(region) + ': ' + '<center: ' + str((centroid[0], centroid[1])) + '>, <area: ' + str(len(points)) + ' pixels>')

        return stats

    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        for region, data in stats.items():
            cv2.putText(image, '*' + str(region) + ',' + str(data[0]) + ',' + str(data[1]), data[0], cv2.FONT_HERSHEY_SIMPLEX, 0.25, 100)

        return image

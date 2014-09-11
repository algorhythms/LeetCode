__author__ = 'Danyang'
class Solution:
    def addBinary_builtin(self, a, b):
        """
        Built-in function
        :param a: string
        :param b: string
        :return: string
        """
        a = int(a, 2)
        b = int(b, 2)
        return bin(a+b)[2:]

    def addBinary(self, a, b):
        """
        Built-in function
        :param a: string
        :param b: string
        :return: string
        """
        if len(a)>len(b):
            a, b = b, a

        a, b = list(a), list(b)

        # from LSB to MSB
        a.reverse()
        b.reverse()
        # b as the base number
        for i in xrange(len(a)):
            if a[i]=="0":  # 0
                continue
            elif b[i]=="0":  # 0+1
                b[i] = "1"
                continue
            else:  # 1+1
                b[i] = "0"

                # carry forward
                if i==len(b)-1:
                    b.append("1")
                else:
                    for j in range(i+1, len(b)):
                        if b[j]=="0":
                            b[j] = "1"
                            break

                        else:
                            b[j] = "0"  # carry forward
                            if j==len(b)-1:
                                b.append("1")
                                break

        b.reverse()
        return "".join(b)  # reversed back

if __name__=="__main__":
    print Solution().addBinary("11", "1")

from decode import decode

# int f(int a, int b) {
#        int j = a + b;
#        return j + 2;
# }
# @O0, -march=rv32i

f = [
 0xfd010113, #               addi    sp,sp,-48
 0x02812623, #               sw      s0,44(sp)
 0x03010413, #               addi    s0,sp,48
 0xfca42e23, #               sw      a0,-36(s0)
 0xfcb42c23, #               sw      a1,-40(s0)
 0xfdc42703, #               lw      a4,-36(s0)
 0xfd842783, #               lw      a5,-40(s0)
 0x00f707b3, #               add     a5,a4,a5
 0xfef42623, #               sw      a5,-20(s0)
 0xfec42783, #               lw      a5,-20(s0)
 0x00278793, #               addi    a5,a5,2
 0x00078513, #               mv      a0,a5
 0x02c12403, #               lw      s0,44(sp)
 0x03010113, #               addi    sp,sp,48
 0x00008067, #               ret
]

for i in f:
  inst = decode(i)
  print (inst)

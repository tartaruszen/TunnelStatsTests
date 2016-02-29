from PacketAnalyzer import PacketAnalyzer
from MetaPacketCap import MetaPacketCap
from PacketDigester import PacketDigester


#if __name__ == "main":
# 1. Read pcap file
# 2. Get specific entropy function,
# 3. "do plot"

# Collect Packet Captures to Analyze
httpMcap = MetaPacketCap("../scapy_tutorial/NewPcaps/TunnelCaps_2011/HTTP.pcap")
httpOvrDnsMetaCap = MetaPacketCap("../scapy_tutorial/NewPcaps/TunnelCaps_2011/HTTPoverDNS.pcap")

ftpMcap = MetaPacketCap("../scapy_tutorial/NewPcaps/TunnelCaps_2011/FTP.pcap")
ftpOvrDnsMetaCap = MetaPacketCap("../scapy_tutorial/NewPcaps/TunnelCaps_2011/FTPoverDNS.pcap")

print("Pcaps Loaded and Initialized ... ")

pktDgstr = PacketDigester()
pktAnlyzr = PacketAnalyzer()

# # Calculate KL-Divergence over 20 Samples: HTTP vs HTTP-over-DNS
# avgKLd20Samples, KLDivVals = pktAnlyzr.calcStatMeasureAvg(
#     "KL-Divergence",
#     pktDgstr.getPopulationLists(
#         httpOvrDnsMetaCap.getDnsPktEntropy(),
#         httpMcap.getHttpReqEntropy()),
#     20)
#
# print("Kullback-Leibler Distance Average of 20 Sampling Rounds: \n"
#        "HTTP and HTTP-over-DNS", avgKLd20Samples)
# pktAnlyzr.doScatterPlot(KLDivVals,'red', 'KL-Divergence', 'Sample Round', 'KL-Distance')
#========

# # Calculate Single Sample KL Divergence: HTTP vs HTTP-over-DNS
# compKLDresult = pktAnlyzr.calcKLDistance(
#     pktAnlyzr.getTwoEquiLenSamples(
#         httpOvrDnsMetaCap.getDnsPktEntropy(),
#         httpMcap.getHttpReqEntropy()))
#
# print("Kullback-Leibler Distance of a Single Sample: ", compKLDresult)
#========

# # Calculate Spearman Ranking Coefficient of Correlation over 20 Samples
# spearman20avg, spearmanVals = pktAnlyzr.calcStatMeasureAvg(
#     "SpearmanR",
#     pktDgstr.getPopulationLists(
#         httpOvrDnsMetaCap.getDnsPktEntropy(),
#         httpMcap.getHttpReqEntropy()),
#     1000)
#
# print("Spearman Ranked Corr Coeff Average of 20 Sampling Rounds: \n"
#       "HTTP and HTTP-over-DNS", spearman20avg)
# pktAnlyzr.doScatterPlot(spearmanVals,'red', 'Spearman', 'Sample Round', 'Correlation Coefficent')
#=========

# # Calculate Single Sample Spearman Ranked coefficient of correlation
# spearmanCoeff = pktAnlyzr.calcSpearman(
#     pktAnlyzr.getTwoEquiLenSamples(httpOvrDnsMetaCap.getDnsPktEntropy(),
#     httpMcap.getHttpReqEntropy()))
#
# print("Spearman Correlation Coefficient: ", spearmanCoeff)
#=========

# # Calculate Pearson Correlation Co-efficient over 20 Samples
# pearson20avg, pearsonVals = pktAnlyzr.calcStatMeasureAvg(
#     "Pearson",
#     pktDgstr.getPopulationLists(
#         httpOvrDnsMetaCap.getDnsPktEntropy(),
#         httpMcap.getHttpReqEntropy()),
#     1000)
#
# print("Pearson Corr Coeff Average of 20 Sampling Rounds: \n"
#       "HTTP and HTTP-over-DNS", pearson20avg)
# pktAnlyzr.doScatterPlot(pearsonVals,'red', 'Pearson', 'Sample Round', 'Correlation Coefficent')
#=========

# # Calculate Single Sample Pearson correlation coefficient
# pearsonCoeff = pktAnlyzr.calcPearson(
#     pktAnlyzr.getTwoEquiLenSamples(httpOvrDnsMetaCap.getDnsPktEntropy(),
#     httpMcap.getHttpReqEntropy()))
#
# print("Pearson Correlation Coefficient: ", pearsonCoeff)
#=========

# Just for getting the variables initialized for plotting (HTTP and HTTP-over-DNS)
httpMcap.getHttpReqEntropy()
httpOvrDnsMetaCap.getDnsPktEntropy()

httpMcap.doPlot("HTTP Request Entropy", "Packet Sequence (Time)", "Byte (Char) Entropy per packet")
#httpOvrDnsMetaCap.doPlot("HTTP Request Entropy", "Packet Sequence (Time)", "Byte (Char) Entropy per packet")

# # Just for getting the variables initialized for plotting (FTP and FTP-over-DNS)
# ftpMcap.getHttpReqEntropy()
# ftpOvrDnsMetaCap.getDnsPktEntropy()
#
# ftpMcap.doPlot("HTTP Request Entropy", "Packet Sequence (Time)", "Byte (Char) Entropy per packet")
# ftpOvrDnsMetaCap.doPlot("HTTP Request Entropy", "Packet Sequence (Time)", "Byte (Char) Entropy per packet")
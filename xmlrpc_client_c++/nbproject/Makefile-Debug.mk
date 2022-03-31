#
# Generated Makefile - do not edit!
#
# Edit the Makefile in the project folder instead (../Makefile). Each target
# has a -pre and a -post target defined where you can add customized code.
#
# This makefile implements configuration specific macros and targets.


# Environment
MKDIR=mkdir
CP=cp
GREP=grep
NM=nm
CCADMIN=CCadmin
RANLIB=ranlib
CC=gcc
CCC=g++
CXX=g++
FC=gfortran
AS=as

# Macros
CND_PLATFORM=GNU-Linux
CND_DLIB_EXT=so
CND_CONF=Debug
CND_DISTDIR=dist
CND_BUILDDIR=build

# Include project Makefile
include Makefile

# Object Directory
OBJECTDIR=${CND_BUILDDIR}/${CND_CONF}/${CND_PLATFORM}

# Object Files
OBJECTFILES= \
	${OBJECTDIR}/XmlRpcClient.o \
	${OBJECTDIR}/XmlRpcDispatch.o \
	${OBJECTDIR}/XmlRpcServer.o \
	${OBJECTDIR}/XmlRpcServerConnection.o \
	${OBJECTDIR}/XmlRpcServerMethod.o \
	${OBJECTDIR}/XmlRpcSocket.o \
	${OBJECTDIR}/XmlRpcSource.o \
	${OBJECTDIR}/XmlRpcUtil.o \
	${OBJECTDIR}/XmlRpcValue.o \
	${OBJECTDIR}/cliente_cmd.o


# C Compiler Flags
CFLAGS=

# CC Compiler Flags
CCFLAGS=
CXXFLAGS=

# Fortran Compiler Flags
FFLAGS=

# Assembler Flags
ASFLAGS=

# Link Libraries and Options
LDLIBSOPTIONS=

# Build Targets
.build-conf: ${BUILD_SUBPROJECTS}
	"${MAKE}"  -f nbproject/Makefile-${CND_CONF}.mk ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/xmlrpc_client_c__

${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/xmlrpc_client_c__: ${OBJECTFILES}
	${MKDIR} -p ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}
	${LINK.cc} -o ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/xmlrpc_client_c__ ${OBJECTFILES} ${LDLIBSOPTIONS}

${OBJECTDIR}/XmlRpcClient.o: XmlRpcClient.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -g -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/XmlRpcClient.o XmlRpcClient.cpp

${OBJECTDIR}/XmlRpcDispatch.o: XmlRpcDispatch.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -g -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/XmlRpcDispatch.o XmlRpcDispatch.cpp

${OBJECTDIR}/XmlRpcServer.o: XmlRpcServer.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -g -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/XmlRpcServer.o XmlRpcServer.cpp

${OBJECTDIR}/XmlRpcServerConnection.o: XmlRpcServerConnection.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -g -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/XmlRpcServerConnection.o XmlRpcServerConnection.cpp

${OBJECTDIR}/XmlRpcServerMethod.o: XmlRpcServerMethod.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -g -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/XmlRpcServerMethod.o XmlRpcServerMethod.cpp

${OBJECTDIR}/XmlRpcSocket.o: XmlRpcSocket.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -g -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/XmlRpcSocket.o XmlRpcSocket.cpp

${OBJECTDIR}/XmlRpcSource.o: XmlRpcSource.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -g -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/XmlRpcSource.o XmlRpcSource.cpp

${OBJECTDIR}/XmlRpcUtil.o: XmlRpcUtil.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -g -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/XmlRpcUtil.o XmlRpcUtil.cpp

${OBJECTDIR}/XmlRpcValue.o: XmlRpcValue.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -g -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/XmlRpcValue.o XmlRpcValue.cpp

${OBJECTDIR}/cliente_cmd.o: cliente_cmd.cpp 
	${MKDIR} -p ${OBJECTDIR}
	${RM} "$@.d"
	$(COMPILE.cc) -g -MMD -MP -MF "$@.d" -o ${OBJECTDIR}/cliente_cmd.o cliente_cmd.cpp

# Subprojects
.build-subprojects:

# Clean Targets
.clean-conf: ${CLEAN_SUBPROJECTS}
	${RM} -r ${CND_BUILDDIR}/${CND_CONF}
	${RM} ${CND_DISTDIR}/${CND_CONF}/${CND_PLATFORM}/xmlrpc_client_c__

# Subprojects
.clean-subprojects:

# Enable dependency checking
.dep.inc: .depcheck-impl

include .dep.inc

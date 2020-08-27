/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 4.8.6
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtGui/QAction>
#include <QtGui/QApplication>
#include <QtGui/QButtonGroup>
#include <QtGui/QCheckBox>
#include <QtGui/QComboBox>
#include <QtGui/QFormLayout>
#include <QtGui/QGroupBox>
#include <QtGui/QHBoxLayout>
#include <QtGui/QHeaderView>
#include <QtGui/QLCDNumber>
#include <QtGui/QLabel>
#include <QtGui/QLayout>
#include <QtGui/QMainWindow>
#include <QtGui/QMenu>
#include <QtGui/QMenuBar>
#include <QtGui/QPushButton>
#include <QtGui/QStatusBar>
#include <QtGui/QTabWidget>
#include <QtGui/QTextEdit>
#include <QtGui/QToolBar>
#include <QtGui/QToolBox>
#include <QtGui/QWidget>
#include "qcustomplot.h"

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *action_load_dump;
    QAction *action_rst;
    QAction *action_close;
    QWidget *centralWidget;
    QTabWidget *tabWidget;
    QWidget *plot;
    QToolBox *toolBox;
    QWidget *ch1;
    QCustomPlot *p_ch1_lo1;
    QCustomPlot *p_ch1_lo2;
    QWidget *horizontalLayoutWidget_3;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_7;
    QLCDNumber *lcd_f0_1;
    QLabel *label_8;
    QLabel *label_9;
    QLCDNumber *lcd_p_1;
    QLabel *label_10;
    QLabel *label_11;
    QComboBox *fstart_comb1;
    QLabel *label_12;
    QComboBox *fend_comb1;
    QLabel *label_13;
    QWidget *horizontalLayoutWidget_4;
    QHBoxLayout *horizontalLayout_4;
    QLabel *label_15;
    QTextEdit *edit_x1;
    QLabel *label_16;
    QTextEdit *edit_y1;
    QWidget *ch2;
    QCustomPlot *p_ch2_lo2;
    QCustomPlot *p_ch2_lo1;
    QWidget *horizontalLayoutWidget_2;
    QHBoxLayout *horizontalLayout_2;
    QLabel *label;
    QLCDNumber *lcd_f0_2;
    QLabel *label_2;
    QLabel *label_5;
    QLCDNumber *lcd_p_2;
    QLabel *label_6;
    QLabel *label_3;
    QComboBox *fstart_comb2;
    QLabel *label_4;
    QComboBox *fend_comb2;
    QLabel *label_14;
    QWidget *horizontalLayoutWidget_5;
    QHBoxLayout *horizontalLayout_5;
    QLabel *label_17;
    QTextEdit *edit_x2;
    QLabel *label_18;
    QTextEdit *edit_y2;
    QWidget *settings;
    QGroupBox *groupBox;
    QWidget *formLayoutWidget;
    QFormLayout *formLayout;
    QLabel *label_19;
    QTextEdit *port_edit;
    QLabel *label_20;
    QTextEdit *baud_edit;
    QLabel *label_21;
    QComboBox *parity_comb;
    QLabel *label_22;
    QComboBox *stp_bts_comb;
    QLabel *label_23;
    QComboBox *byte_comb;
    QPushButton *sve_uart;
    QWidget *horizontalLayoutWidget;
    QHBoxLayout *horizontalLayout;
    QCheckBox *cont_cb;
    QMenuBar *menuBar;
    QMenu *menuPlotter;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(938, 740);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        action_load_dump = new QAction(MainWindow);
        action_load_dump->setObjectName(QString::fromUtf8("action_load_dump"));
        action_load_dump->setCheckable(false);
        action_rst = new QAction(MainWindow);
        action_rst->setObjectName(QString::fromUtf8("action_rst"));
        action_close = new QAction(MainWindow);
        action_close->setObjectName(QString::fromUtf8("action_close"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        sizePolicy.setHeightForWidth(centralWidget->sizePolicy().hasHeightForWidth());
        centralWidget->setSizePolicy(sizePolicy);
        centralWidget->setLayoutDirection(Qt::LeftToRight);
        tabWidget = new QTabWidget(centralWidget);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setGeometry(QRect(10, 20, 911, 651));
        tabWidget->setTabPosition(QTabWidget::South);
        plot = new QWidget();
        plot->setObjectName(QString::fromUtf8("plot"));
        sizePolicy.setHeightForWidth(plot->sizePolicy().hasHeightForWidth());
        plot->setSizePolicy(sizePolicy);
        plot->setContextMenuPolicy(Qt::DefaultContextMenu);
        toolBox = new QToolBox(plot);
        toolBox->setObjectName(QString::fromUtf8("toolBox"));
        toolBox->setGeometry(QRect(0, 0, 911, 611));
        ch1 = new QWidget();
        ch1->setObjectName(QString::fromUtf8("ch1"));
        ch1->setGeometry(QRect(0, 0, 911, 555));
        p_ch1_lo1 = new QCustomPlot(ch1);
        p_ch1_lo1->setObjectName(QString::fromUtf8("p_ch1_lo1"));
        p_ch1_lo1->setGeometry(QRect(10, 0, 891, 241));
        p_ch1_lo2 = new QCustomPlot(ch1);
        p_ch1_lo2->setObjectName(QString::fromUtf8("p_ch1_lo2"));
        p_ch1_lo2->setGeometry(QRect(10, 270, 891, 241));
        horizontalLayoutWidget_3 = new QWidget(ch1);
        horizontalLayoutWidget_3->setObjectName(QString::fromUtf8("horizontalLayoutWidget_3"));
        horizontalLayoutWidget_3->setGeometry(QRect(10, 520, 512, 25));
        horizontalLayout_3 = new QHBoxLayout(horizontalLayoutWidget_3);
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        label_7 = new QLabel(horizontalLayoutWidget_3);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        horizontalLayout_3->addWidget(label_7);

        lcd_f0_1 = new QLCDNumber(horizontalLayoutWidget_3);
        lcd_f0_1->setObjectName(QString::fromUtf8("lcd_f0_1"));

        horizontalLayout_3->addWidget(lcd_f0_1);

        label_8 = new QLabel(horizontalLayoutWidget_3);
        label_8->setObjectName(QString::fromUtf8("label_8"));

        horizontalLayout_3->addWidget(label_8);

        label_9 = new QLabel(horizontalLayoutWidget_3);
        label_9->setObjectName(QString::fromUtf8("label_9"));

        horizontalLayout_3->addWidget(label_9);

        lcd_p_1 = new QLCDNumber(horizontalLayoutWidget_3);
        lcd_p_1->setObjectName(QString::fromUtf8("lcd_p_1"));

        horizontalLayout_3->addWidget(lcd_p_1);

        label_10 = new QLabel(horizontalLayoutWidget_3);
        label_10->setObjectName(QString::fromUtf8("label_10"));

        horizontalLayout_3->addWidget(label_10);

        label_11 = new QLabel(horizontalLayoutWidget_3);
        label_11->setObjectName(QString::fromUtf8("label_11"));

        horizontalLayout_3->addWidget(label_11);

        fstart_comb1 = new QComboBox(horizontalLayoutWidget_3);
        fstart_comb1->setObjectName(QString::fromUtf8("fstart_comb1"));

        horizontalLayout_3->addWidget(fstart_comb1);

        label_12 = new QLabel(horizontalLayoutWidget_3);
        label_12->setObjectName(QString::fromUtf8("label_12"));

        horizontalLayout_3->addWidget(label_12);

        fend_comb1 = new QComboBox(horizontalLayoutWidget_3);
        fend_comb1->setObjectName(QString::fromUtf8("fend_comb1"));

        horizontalLayout_3->addWidget(fend_comb1);

        label_13 = new QLabel(horizontalLayoutWidget_3);
        label_13->setObjectName(QString::fromUtf8("label_13"));

        horizontalLayout_3->addWidget(label_13);

        horizontalLayoutWidget_4 = new QWidget(ch1);
        horizontalLayoutWidget_4->setObjectName(QString::fromUtf8("horizontalLayoutWidget_4"));
        horizontalLayoutWidget_4->setGeometry(QRect(360, 240, 186, 32));
        horizontalLayout_4 = new QHBoxLayout(horizontalLayoutWidget_4);
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        horizontalLayout_4->setSizeConstraint(QLayout::SetFixedSize);
        horizontalLayout_4->setContentsMargins(0, 0, 0, 0);
        label_15 = new QLabel(horizontalLayoutWidget_4);
        label_15->setObjectName(QString::fromUtf8("label_15"));

        horizontalLayout_4->addWidget(label_15);

        edit_x1 = new QTextEdit(horizontalLayoutWidget_4);
        edit_x1->setObjectName(QString::fromUtf8("edit_x1"));
        edit_x1->setEnabled(true);
        edit_x1->setMinimumSize(QSize(0, 29));
        edit_x1->setMaximumSize(QSize(64, 29));
        QFont font;
        font.setPointSize(8);
        edit_x1->setFont(font);
        edit_x1->setFocusPolicy(Qt::NoFocus);
        edit_x1->setAutoFillBackground(false);
        edit_x1->setInputMethodHints(Qt::ImhNone);
        edit_x1->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        edit_x1->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        edit_x1->setTextInteractionFlags(Qt::NoTextInteraction);

        horizontalLayout_4->addWidget(edit_x1);

        label_16 = new QLabel(horizontalLayoutWidget_4);
        label_16->setObjectName(QString::fromUtf8("label_16"));

        horizontalLayout_4->addWidget(label_16);

        edit_y1 = new QTextEdit(horizontalLayoutWidget_4);
        edit_y1->setObjectName(QString::fromUtf8("edit_y1"));
        edit_y1->setMinimumSize(QSize(0, 29));
        edit_y1->setMaximumSize(QSize(64, 29));
        edit_y1->setFont(font);
        edit_y1->setFocusPolicy(Qt::NoFocus);
        edit_y1->setAutoFillBackground(false);
        edit_y1->setInputMethodHints(Qt::ImhNone);
        edit_y1->setFrameShape(QFrame::StyledPanel);
        edit_y1->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        edit_y1->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        edit_y1->setUndoRedoEnabled(true);
        edit_y1->setTextInteractionFlags(Qt::NoTextInteraction);

        horizontalLayout_4->addWidget(edit_y1);

        toolBox->addItem(ch1, QString::fromUtf8("\320\272\320\260\320\275\320\260\320\273 1"));
        ch2 = new QWidget();
        ch2->setObjectName(QString::fromUtf8("ch2"));
        ch2->setGeometry(QRect(0, 0, 911, 555));
        p_ch2_lo2 = new QCustomPlot(ch2);
        p_ch2_lo2->setObjectName(QString::fromUtf8("p_ch2_lo2"));
        p_ch2_lo2->setGeometry(QRect(10, 260, 891, 251));
        p_ch2_lo1 = new QCustomPlot(ch2);
        p_ch2_lo1->setObjectName(QString::fromUtf8("p_ch2_lo1"));
        p_ch2_lo1->setGeometry(QRect(10, 0, 891, 231));
        horizontalLayoutWidget_2 = new QWidget(ch2);
        horizontalLayoutWidget_2->setObjectName(QString::fromUtf8("horizontalLayoutWidget_2"));
        horizontalLayoutWidget_2->setGeometry(QRect(10, 520, 550, 25));
        horizontalLayout_2 = new QHBoxLayout(horizontalLayoutWidget_2);
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        label = new QLabel(horizontalLayoutWidget_2);
        label->setObjectName(QString::fromUtf8("label"));

        horizontalLayout_2->addWidget(label);

        lcd_f0_2 = new QLCDNumber(horizontalLayoutWidget_2);
        lcd_f0_2->setObjectName(QString::fromUtf8("lcd_f0_2"));

        horizontalLayout_2->addWidget(lcd_f0_2);

        label_2 = new QLabel(horizontalLayoutWidget_2);
        label_2->setObjectName(QString::fromUtf8("label_2"));

        horizontalLayout_2->addWidget(label_2);

        label_5 = new QLabel(horizontalLayoutWidget_2);
        label_5->setObjectName(QString::fromUtf8("label_5"));

        horizontalLayout_2->addWidget(label_5);

        lcd_p_2 = new QLCDNumber(horizontalLayoutWidget_2);
        lcd_p_2->setObjectName(QString::fromUtf8("lcd_p_2"));

        horizontalLayout_2->addWidget(lcd_p_2);

        label_6 = new QLabel(horizontalLayoutWidget_2);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        horizontalLayout_2->addWidget(label_6);

        label_3 = new QLabel(horizontalLayoutWidget_2);
        label_3->setObjectName(QString::fromUtf8("label_3"));

        horizontalLayout_2->addWidget(label_3);

        fstart_comb2 = new QComboBox(horizontalLayoutWidget_2);
        fstart_comb2->setObjectName(QString::fromUtf8("fstart_comb2"));

        horizontalLayout_2->addWidget(fstart_comb2);

        label_4 = new QLabel(horizontalLayoutWidget_2);
        label_4->setObjectName(QString::fromUtf8("label_4"));

        horizontalLayout_2->addWidget(label_4);

        fend_comb2 = new QComboBox(horizontalLayoutWidget_2);
        fend_comb2->setObjectName(QString::fromUtf8("fend_comb2"));

        horizontalLayout_2->addWidget(fend_comb2);

        label_14 = new QLabel(horizontalLayoutWidget_2);
        label_14->setObjectName(QString::fromUtf8("label_14"));

        horizontalLayout_2->addWidget(label_14);

        horizontalLayoutWidget_5 = new QWidget(ch2);
        horizontalLayoutWidget_5->setObjectName(QString::fromUtf8("horizontalLayoutWidget_5"));
        horizontalLayoutWidget_5->setGeometry(QRect(350, 230, 186, 32));
        horizontalLayout_5 = new QHBoxLayout(horizontalLayoutWidget_5);
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        horizontalLayout_5->setSizeConstraint(QLayout::SetFixedSize);
        horizontalLayout_5->setContentsMargins(0, 0, 0, 0);
        label_17 = new QLabel(horizontalLayoutWidget_5);
        label_17->setObjectName(QString::fromUtf8("label_17"));

        horizontalLayout_5->addWidget(label_17);

        edit_x2 = new QTextEdit(horizontalLayoutWidget_5);
        edit_x2->setObjectName(QString::fromUtf8("edit_x2"));
        edit_x2->setEnabled(true);
        edit_x2->setMinimumSize(QSize(0, 29));
        edit_x2->setMaximumSize(QSize(64, 29));
        edit_x2->setFont(font);
        edit_x2->setFocusPolicy(Qt::NoFocus);
        edit_x2->setAutoFillBackground(false);
        edit_x2->setInputMethodHints(Qt::ImhNone);
        edit_x2->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        edit_x2->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        edit_x2->setTextInteractionFlags(Qt::NoTextInteraction);

        horizontalLayout_5->addWidget(edit_x2);

        label_18 = new QLabel(horizontalLayoutWidget_5);
        label_18->setObjectName(QString::fromUtf8("label_18"));

        horizontalLayout_5->addWidget(label_18);

        edit_y2 = new QTextEdit(horizontalLayoutWidget_5);
        edit_y2->setObjectName(QString::fromUtf8("edit_y2"));
        edit_y2->setMinimumSize(QSize(0, 29));
        edit_y2->setMaximumSize(QSize(64, 29));
        edit_y2->setFont(font);
        edit_y2->setFocusPolicy(Qt::NoFocus);
        edit_y2->setAutoFillBackground(false);
        edit_y2->setInputMethodHints(Qt::ImhNone);
        edit_y2->setFrameShape(QFrame::StyledPanel);
        edit_y2->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        edit_y2->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        edit_y2->setUndoRedoEnabled(true);
        edit_y2->setTextInteractionFlags(Qt::NoTextInteraction);

        horizontalLayout_5->addWidget(edit_y2);

        toolBox->addItem(ch2, QString::fromUtf8("\320\272\320\260\320\275\320\260\320\273 2"));
        tabWidget->addTab(plot, QString());
        settings = new QWidget();
        settings->setObjectName(QString::fromUtf8("settings"));
        QSizePolicy sizePolicy1(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(settings->sizePolicy().hasHeightForWidth());
        settings->setSizePolicy(sizePolicy1);
        groupBox = new QGroupBox(settings);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setGeometry(QRect(10, 20, 391, 221));
        formLayoutWidget = new QWidget(groupBox);
        formLayoutWidget->setObjectName(QString::fromUtf8("formLayoutWidget"));
        formLayoutWidget->setGeometry(QRect(19, 40, 361, 141));
        formLayout = new QFormLayout(formLayoutWidget);
        formLayout->setSpacing(6);
        formLayout->setContentsMargins(11, 11, 11, 11);
        formLayout->setObjectName(QString::fromUtf8("formLayout"));
        formLayout->setFieldGrowthPolicy(QFormLayout::AllNonFixedFieldsGrow);
        formLayout->setContentsMargins(0, 0, 0, 0);
        label_19 = new QLabel(formLayoutWidget);
        label_19->setObjectName(QString::fromUtf8("label_19"));

        formLayout->setWidget(0, QFormLayout::LabelRole, label_19);

        port_edit = new QTextEdit(formLayoutWidget);
        port_edit->setObjectName(QString::fromUtf8("port_edit"));
        port_edit->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        port_edit->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);

        formLayout->setWidget(0, QFormLayout::FieldRole, port_edit);

        label_20 = new QLabel(formLayoutWidget);
        label_20->setObjectName(QString::fromUtf8("label_20"));

        formLayout->setWidget(1, QFormLayout::LabelRole, label_20);

        baud_edit = new QTextEdit(formLayoutWidget);
        baud_edit->setObjectName(QString::fromUtf8("baud_edit"));
        baud_edit->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        baud_edit->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);

        formLayout->setWidget(1, QFormLayout::FieldRole, baud_edit);

        label_21 = new QLabel(formLayoutWidget);
        label_21->setObjectName(QString::fromUtf8("label_21"));

        formLayout->setWidget(2, QFormLayout::LabelRole, label_21);

        parity_comb = new QComboBox(formLayoutWidget);
        parity_comb->setObjectName(QString::fromUtf8("parity_comb"));

        formLayout->setWidget(2, QFormLayout::FieldRole, parity_comb);

        label_22 = new QLabel(formLayoutWidget);
        label_22->setObjectName(QString::fromUtf8("label_22"));

        formLayout->setWidget(3, QFormLayout::LabelRole, label_22);

        stp_bts_comb = new QComboBox(formLayoutWidget);
        stp_bts_comb->setObjectName(QString::fromUtf8("stp_bts_comb"));

        formLayout->setWidget(3, QFormLayout::FieldRole, stp_bts_comb);

        label_23 = new QLabel(formLayoutWidget);
        label_23->setObjectName(QString::fromUtf8("label_23"));

        formLayout->setWidget(4, QFormLayout::LabelRole, label_23);

        byte_comb = new QComboBox(formLayoutWidget);
        byte_comb->setObjectName(QString::fromUtf8("byte_comb"));

        formLayout->setWidget(4, QFormLayout::FieldRole, byte_comb);

        sve_uart = new QPushButton(groupBox);
        sve_uart->setObjectName(QString::fromUtf8("sve_uart"));
        sve_uart->setGeometry(QRect(20, 190, 81, 22));
        tabWidget->addTab(settings, QString());
        horizontalLayoutWidget = new QWidget(centralWidget);
        horizontalLayoutWidget->setObjectName(QString::fromUtf8("horizontalLayoutWidget"));
        horizontalLayoutWidget->setGeometry(QRect(9, 1, 681, 22));
        horizontalLayout = new QHBoxLayout(horizontalLayoutWidget);
        horizontalLayout->setSpacing(6);
        horizontalLayout->setContentsMargins(11, 11, 11, 11);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        cont_cb = new QCheckBox(horizontalLayoutWidget);
        cont_cb->setObjectName(QString::fromUtf8("cont_cb"));

        horizontalLayout->addWidget(cont_cb);

        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 938, 19));
        menuPlotter = new QMenu(menuBar);
        menuPlotter->setObjectName(QString::fromUtf8("menuPlotter"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuPlotter->menuAction());
        menuPlotter->addAction(action_load_dump);
        menuPlotter->addAction(action_rst);
        menuPlotter->addAction(action_close);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(1);
        toolBox->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Plotter", 0, QApplication::UnicodeUTF8));
        action_load_dump->setText(QApplication::translate("MainWindow", "\320\267\320\260\320\263\321\200\321\203\320\267\320\270\321\202\321\214 \320\264\320\260\320\274\320\277", 0, QApplication::UnicodeUTF8));
        action_rst->setText(QApplication::translate("MainWindow", "\321\201\320\261\321\200\320\276\321\201\320\270\321\202\321\214 \320\274\320\276\320\264\321\203\320\273\321\214", 0, QApplication::UnicodeUTF8));
        action_close->setText(QApplication::translate("MainWindow", "\320\267\320\260\320\272\321\200\321\213\321\202\321\214", 0, QApplication::UnicodeUTF8));
        label_7->setText(QApplication::translate("MainWindow", "<html><head/><body><p>f0=</p></body></html>", 0, QApplication::UnicodeUTF8));
        label_8->setText(QApplication::translate("MainWindow", "Hz,", 0, QApplication::UnicodeUTF8));
        label_9->setText(QApplication::translate("MainWindow", "P=", 0, QApplication::UnicodeUTF8));
        label_10->setText(QApplication::translate("MainWindow", "dBm,", 0, QApplication::UnicodeUTF8));
        label_11->setText(QApplication::translate("MainWindow", "Fstart", 0, QApplication::UnicodeUTF8));
        label_12->setText(QApplication::translate("MainWindow", "Fend", 0, QApplication::UnicodeUTF8));
        label_13->setText(QApplication::translate("MainWindow", "kHz", 0, QApplication::UnicodeUTF8));
        label_15->setText(QApplication::translate("MainWindow", "x=", 0, QApplication::UnicodeUTF8));
        label_16->setText(QApplication::translate("MainWindow", "y=", 0, QApplication::UnicodeUTF8));
        toolBox->setItemText(toolBox->indexOf(ch1), QApplication::translate("MainWindow", "\320\272\320\260\320\275\320\260\320\273 1", 0, QApplication::UnicodeUTF8));
        label->setText(QApplication::translate("MainWindow", "<html><head/><body><p>f0=</p></body></html>", 0, QApplication::UnicodeUTF8));
        label_2->setText(QApplication::translate("MainWindow", "Hz,", 0, QApplication::UnicodeUTF8));
        label_5->setText(QApplication::translate("MainWindow", "P=", 0, QApplication::UnicodeUTF8));
        label_6->setText(QApplication::translate("MainWindow", "dBm,", 0, QApplication::UnicodeUTF8));
        label_3->setText(QApplication::translate("MainWindow", "Fstart", 0, QApplication::UnicodeUTF8));
        label_4->setText(QApplication::translate("MainWindow", "Fend", 0, QApplication::UnicodeUTF8));
        label_14->setText(QApplication::translate("MainWindow", "kHz", 0, QApplication::UnicodeUTF8));
        label_17->setText(QApplication::translate("MainWindow", "x=", 0, QApplication::UnicodeUTF8));
        label_18->setText(QApplication::translate("MainWindow", "y=", 0, QApplication::UnicodeUTF8));
        toolBox->setItemText(toolBox->indexOf(ch2), QApplication::translate("MainWindow", "\320\272\320\260\320\275\320\260\320\273 2", 0, QApplication::UnicodeUTF8));
        tabWidget->setTabText(tabWidget->indexOf(plot), QApplication::translate("MainWindow", "\320\263\321\200\320\260\321\204\320\270\320\272\320\270", 0, QApplication::UnicodeUTF8));
        groupBox->setTitle(QApplication::translate("MainWindow", "UART", 0, QApplication::UnicodeUTF8));
        label_19->setText(QApplication::translate("MainWindow", "port", 0, QApplication::UnicodeUTF8));
        port_edit->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/dev/ttyUSB0</p></body></html>", 0, QApplication::UnicodeUTF8));
        label_20->setText(QApplication::translate("MainWindow", "baudrate", 0, QApplication::UnicodeUTF8));
        baud_edit->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">115200</p></body></html>", 0, QApplication::UnicodeUTF8));
        label_21->setText(QApplication::translate("MainWindow", "parity", 0, QApplication::UnicodeUTF8));
        label_22->setText(QApplication::translate("MainWindow", "stopbits", 0, QApplication::UnicodeUTF8));
        label_23->setText(QApplication::translate("MainWindow", "bytesizes", 0, QApplication::UnicodeUTF8));
        sve_uart->setText(QApplication::translate("MainWindow", "\321\201\320\276\321\205\321\200\320\260\320\275\320\270\321\202\321\214", 0, QApplication::UnicodeUTF8));
        tabWidget->setTabText(tabWidget->indexOf(settings), QApplication::translate("MainWindow", "\320\275\320\260\321\201\321\202\321\200\320\276\320\271\320\272\320\270", 0, QApplication::UnicodeUTF8));
        cont_cb->setText(QApplication::translate("MainWindow", "\320\275\320\265\320\277\321\200\320\265\321\200\321\213\320\262\320\275\321\213\320\265 \320\270\320\267\320\274\320\265\321\200\320\265\320\275\320\270\321\217", 0, QApplication::UnicodeUTF8));
        menuPlotter->setTitle(QApplication::translate("MainWindow", "File", 0, QApplication::UnicodeUTF8));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
